# Pipeline Panic

A demo Python FastAPI project with a CI/CD pipeline containing seeded bugs for educational purposes.

## Installation



1. **Install dependencies:**
	```powershell
	pip install -r requirements.txt
	```

2. **Run the API locally:**
	```powershell
	uvicorn app.main:app --reload
	```

3. **Run tests:**
	```powershell
	pytest
	```

4. **Lint the code:**
	```powershell
	flake8 app/
	```

## Seeded Bugs and How to Fix Them

### 1. Broken Matrix Jobs
**Bug:** The CI matrix runs on both Ubuntu and Windows, but may fail on Windows due to path issues or missing dependencies.
**Fix:** Add OS-specific install steps or limit matrix to supported OS. Example:
```yaml
strategy:
  matrix:
	 os: [ubuntu-latest] # Remove windows-latest if not supported
```
Or add conditional steps for Windows.

### 2. Wrong Cache Keys
**Bug:** The cache key uses `runner.os` and `requirements.txt` hash, but may not restore properly if requirements change or on Windows.
**Fix:** Use more robust cache keys and ensure cache paths are correct for each OS. Example:
```yaml
key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}-${{ github.ref }}
```

### 3. Leaked Secrets
**Bug:** The pipeline exposes `SECRET_KEY` as an environment variable in the test step.
**Fix:** Use a secrets manager (e.g., HashiCorp Vault) and avoid printing secrets in logs. Remove direct usage and fetch secrets securely.

### 4. Environment Mismatch (Dev≠CI)
**Bug:** The API behaves differently based on `APP_ENV`, but `prod` is not handled, causing test failures.
**Fix:** Ensure all environments are handled in code and tests. Update `main.py`:
```python
if env == "ci":
	 ...
elif env == "prod":
	 return {"message": "Hello from Prod!"}
```

### 5. Flaky Tests
**Bug:** The test for `/` endpoint passes for both Dev and CI, but is not deterministic. Parametrized test fails for `prod`.
**Fix:** Make tests deterministic and handle all cases in the API. Ensure all expected outputs are covered and avoid randomness.

---