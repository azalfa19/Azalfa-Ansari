# Secure Password Generator Utility

## 💡 Overview of the Project

[cite_start]This project is a command-line interface (CLI) application designed to generate highly secure, random passwords. [cite_start]Its primary objective is to allow users to quickly create strong credentials of a customizable length, ensuring a balanced inclusion of uppercase letters, lowercase letters, numbers, and symbols to maximize security and meet modern password complexity standards[cite: 8, 9, 12].

## ✨ Features (Functional Requirements)

[cite_start]This project includes the following high-level features:

* [cite_start]**Customizable Password Generation:** Allows the user to specify the exact desired length of the password (Data input & processing)[cite: 26].
* [cite_start]**Character Pool Logic:** Manages the selection and pooling of characters (letters, digits, symbols) to ensure diversity (Three major functional modules)[cite: 21].
* [cite_start]**Guaranteed Complexity:** The system ensures that the generated password contains at least one of each required character type (Error handling strategy/Validation)[cite: 41, 54].
* [cite_start]**Clear I/O Structure:** Provides a straightforward command-line interface for inputting length and clear output for displaying the generated password[cite: 22].

## 🛠️ Technologies & Tools Used

| Component | Technology / Tool | Rationale |
| :--- | :--- | :--- |
| **Programming Language** | Python 3.x | Standard language used for implementation. |
| **Libraries** | `random`, `string` | Utilized for core generation logic and defining character sets. |
| **Version Control** | Git | [cite_start]Used for version control management[cite: 55]. |
| **Repository Host** | GitHub | [cite_start]Host for source code and submission requirement[cite: 84]. |

## 🚀 Steps to Install & Run the Project

### Prerequisites

You must have **Python 3.x** installed on your system.

### Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YourUsername/secure-password-generator.git](https://github.com/YourUsername/secure-password-generator.git)
    cd secure-password-generator
    ```

2.  **No external libraries are required.** The project uses only standard Python libraries.

### Execution

Run the main script from your terminal:

```bash
python password_generator.py

The application will prompt you for input:

Welcome to the Secure Password Generator!
Enter the desired length of the password (e.g., 16):

🧪 Instructions for Testing
This project incorporates validation and basic testing.


Validation Tests
Length Input Validation: When prompted for length, enter non-integer values (e.g., abc or 12.5). The system should display an error and re-prompt for valid input.

Minimum Length Check (Non-Functional - Reliability): Attempt to enter an extremely short length (e.g., 1 or 2). The system should ideally enforce a minimum length constraint (e.g., 4) for security and reliably generate a password of at least that length.

Functional Verification
Execute the script and verify the following:

Character Diversity: Manually check several generated passwords (e.g., 5 runs). Each result must contain at least one uppercase letter, one lowercase letter, one digit, and one symbol.


Length Accuracy: The length of the generated string must exactly match the number specified by the user.

