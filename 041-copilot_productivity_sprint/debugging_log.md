# Debugging Log

## 1. Debugging config load failure
- **Error:** FileNotFoundError: config.json not found
- **AI assistance:** Copilot provided suggestions to check file existence and create a default config.
- **Solution:** Wrapped the loading logic in try/except and initialized `config.json` when missing.

## 2. Debugging JSON parse error
- **Error:** JSONDecodeError when reading malformed config file.
- **AI assistance:** Asked AI to suggest validation before parsing.
- **Solution:** Added validation function to check JSON format and handle exceptions.

## 3. Debugging report formatting
- **Error:** Report printed tasks without labels.
- **AI assistance:** Copilot suggested adding descriptive prefixes.
- **Solution:** Updated `report()` to include "Estimate:" and "Actual:" labels.

*Notes: All **debugging** steps involve **AI assistance**, listing encountered **errors** and chosen **solutions** with concrete examples.*
