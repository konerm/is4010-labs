# Lab 02 CLI comparison journal

Do not include passwords, tokens, API keys, or complete authentication output.

## Tool check

### GitHub Copilot CLI

I installed and authenticated GitHub Copilot CLI. Version: 1.0.83.

### Antigravity CLI

I installed and authenticated Antigravity CLI. Version: 1.1.27.

## Shared task

### Shared prompt

Paste the exact prompt you submitted to both CLI tools.

```text
Write a pyton function named count_vowels(text: str) -> int that counts a, e, i, o, and u wihtout regard to case, and does not count y.
```

### Copilot CLI observations

Copilot CLI suggested converting the text to lowercase and then counting each character that appears in "aeiou". The response was short and eassy to understand. It followed the requirement not to count y and handled uppercase vowels by using lowercase conversion. I would verify the suggestion with the course tests, especially using uppercase letters, no vowels, and words containing y.

### Antigravity CLI observations

Antigravity CLI suggested converting the text to lowercase and counting characters that appear in a collection containing only a, e, i, o, and u. It used a generator expression with sum and clearly explanined that y should not be counted. I would verify the result with the course tests, espeically empty strings, mixed uppercase and lowercase text, and words that contain y but no standart vowels.

### Comparison

Both Copilot CLI and Antigravity CLI gave correct approaches for counting vowels. Both suggested converting the text to lowercase so uppercase and lowercase vowels are treated the same, and both excluded y from the vowel list. Copilot gave a shorter and more direct response, while Antigravoty explained more details about why the approach works and discussed edge cases such as empty strings, mixed case, and words contianing only y. I think both approaches are useful, but I would select the Antigravity approach because the explanation was clearer and gave more information to verify the behavior. I would still use the course test to comfirm that the final code matches the required function contract.

## Test-guided implementation

The course tests helped me verify that the final code matched the required function behavior. At first, the test run failed because lab02.py did not exist, so I created the file amd added the three required functions. After that, another test run showed an indentation error on the is_even function, so I corrected the spacing and saved the file again. When I reran the tests, the function tests passed, including the greeting tests, even number tests, and vowel counting tests. This showed that the final code handled uppercase vowels, empty text and y correctly. I used the test results to comfirm that the final behavior matches the function contracts from the lab instructions. 
## Preferred tool combination

For my workflow, I prefer using VS Code with the integrated terminal because it keeps the code, files and command line in one place. GitHub Copilot CLI was useful because it gave a shortt and direct suggestion for the count_vowels function. Antigravity CLI was also useful because it gave a more detailed explanation and discussed edge cases such as empty strings, mixed case, and words contraning y. I would currently prefer using VS Code, the terminal and Antigravity CLI together because the explanation helped me understand what the code was doing before I test it. I would choose Copilot CLI instead when I need a faster and shorter ansswer for a simple task.
