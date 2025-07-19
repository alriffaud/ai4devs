# Setup Notes for AI Coding Environment

This document describes how the AI assistant was installed, configured, and tested to verify basic functionality.

---

## 1. AI Assistant Installation

- **AI assistant chosen:** GitHub Copilot  
- **Installation steps:**  
  1. Open **Visual Studio Code** (v1.80+).  
  2. Go to **Extensions** panel.  
  3. Search for **“GitHub Copilot”** and click **Install**.  
  4. After installation, you should see the Copilot icon in the sidebar.  
- **Status:** AI assistant successfully **installed**.

---

## 2. Configuration

- **Authentication:**  
  - Signed in with GitHub account that has Copilot license.  
  - Verified token in `~/.config/Code/User/settings.json`.  
- **Settings adjustments:**  
  ```jsonc
  // VS Code user settings
  {
    "github.copilot.enable": true,
    "github.copilot.inlineSuggest.enable": true,
    "editor.quickSuggestions": {
      "other": true,
      "comments": false,
      "strings": false
    }
  }
  ```  
- **Configuration file location:**  
  - `settings.json` under your VS Code user directory.  
- **Notes:** You can switch between “inline” and “chat” modes in the Copilot pane.

---

## 3. Initial Testing

### 3.1 Hello World Example

1. **Create a new file** `hello.py` with:
   ```python
   # hello.py
   def hello_world():
       # TODO: Use AI assistant to generate this function
       pass
   ```
2. **Invoke Copilot suggestion** by typing inside the function body.  
3. Accept the suggestion. The function should become:
   ```python
   def hello_world():
       print("Hello, World!")
   ```
4. **Run**:
   ```bash
   python hello.py
   ```
5. **Expected output:**  
   ```
   Hello, World!
   ```

### 3.2 Verifying Functionality

- **Test script:**  
  ```python
  # test_hello.py
  from hello import hello_world

  def test_output(capsys):
      hello_world()
      captured = capsys.readouterr()
      assert captured.out.strip() == "Hello, World!"
  ```
- **Run tests** with pytest:
  ```bash
  pytest test_hello.py
  ```
- **Result:** All tests **passed**, confirming Copilot-generated **Hello World** function works as expected.

---

## 4. Summary

- The **AI assistant** is now **installed**, **configured**, and **tested** for basic code generation.  
- Configuration settings were saved to `settings.json` under user preferences.  
- A simple **Hello World** example verifies core **functionality**.  
- Future work: expand tests to cover more complex snippets and ensure reliability under different prompt styles.
