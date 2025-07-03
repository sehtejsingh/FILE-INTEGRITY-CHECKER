# FILE-INTEGRITY-CHECKER

*Company*: CODTECH IT SOLUTION

*Name*: SEHTEJ SINGH

*Itern ID*: : CT04DH922

*Domain*: CYBERSECURITY AND ETHICAL HACKING

*Duration*: 4 Week

*Mentor*: Neela Santosh

##In this cybersecurity project, we designed and implemented a File Change Monitoring Tool using Python. This tool helps detect any unauthorized changes in files within a specified directory by calculating and comparing cryptographic hash values (SHA-256). The process of hash comparison is a foundational technique in cybersecurity for maintaining data integrity.

The key takeaway from this project is the understanding and application of hash functions. A hash function takes input data and returns a fixed-size string (hash) that uniquely represents the input. Even a tiny change in the file leads to a completely different hash. This property is crucial in detecting file tampering, which may occur due to malware infections, insider attacks, or accidental modifications.

Another important concept learned is state management. The tool stores hash values in a JSON file, which acts as a baseline for comparison. Each time the tool runs, it re-scans the directory, computes new hash values, and compares them with the stored baseline to detect any changes. This teaches us how to persist and manage data securely over time.

We also gain insights into filesystem traversal and directory scanning using Python’s os module. This is essential knowledge when dealing with real-world file systems and security audits. We explored how to automate file verification across subdirectories and how to handle exceptions like missing or deleted files safely.

From a security perspective, this tool illustrates the principle of confidentiality, integrity, and availability (CIA). In particular, it focuses on integrity—ensuring that information has not been altered in an unauthorized way. Organizations can integrate such tools in larger Intrusion Detection Systems (IDS) to monitor sensitive configuration files or log files that should remain unchanged.

By simulating a real-world scenario, we better understand why file monitoring is critical in cybersecurity. For instance, if a key system file is modified without authorization, it might be the sign of a security breach. Monitoring tools like this can trigger alerts and prompt immediate action.


## Output:

![Image](https://github.com/user-attachments/assets/6dc3d006-d21a-4e4d-aac5-026da112047f)

Lastly, working on this project improves our problem-solving skills, Python programming expertise, and project documentation habits. In future extensions, we can add email notifications, logging, continuous monitoring, or even a graphical interface.

In conclusion, this file monitoring tool not only demonstrates a practical application of cryptographic concepts but also strengthens our foundation in cybersecurity. It teaches us how to detect anomalies, maintain system integrity, and automate security checks—skills that are essential for any ethical hacker or cybersecurity professional.
