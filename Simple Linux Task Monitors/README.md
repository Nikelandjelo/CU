Using a language of your choice write a program that queries /proc to find information about current processes.
IMPORTANT: For full marks, you need to deal directly with /proc. Using libraries like pythons psutil will result in reduced marks.

For the Standard Task The Program should (15 Marks):

- Display the number and type of CPU's in the system
- Display the current load average of the system
- Display the current count of Processes running on the system

Advanced Task:
One of the stages of a pen-test might be to identify scheduled tasks (for example cronjobs) we can do this by monitoring the running
processes and informing the user if there are any changes.
- Modify the program so that it monitors the processes currently running on the system, and alerts the user when a new process starts,
or one is closed.
