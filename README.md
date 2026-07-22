# Employee Salary Analysis using MapReduce (Python)

## Project Name
Employee Salary Analysis using MapReduce

## Description
This project uses the MapReduce programming model in Python to calculate the total salary of employees in each department.

## Project Structure

EmployeeSalaryMapReduce/
│
├── input.txt
├── splitter.py
├── mapper.py
├── partitioner.py
├── sorter.py
├── reducer.py
├── master.py
├── chunk1.txt
├── chunk2.txt
├── map1.txt
├── map2.txt
├── partitions/
│   ├── partition0.txt
│   └── partition1.txt
└── output/
    └── result.txt

## Input Format

EmployeeID,EmployeeName,Department,Salary

Example:

101,Ravi,HR,25000
102,Priya,IT,40000
103,Arun,Finance,35000

## Execution

Run the project using:

```bash
python master.py

Project Flow

Input File
     ↓
Splitter
     ↓
Mapper
     ↓
Partitioner
     ↓
Sorter
     ↓
Reducer
     ↓
Result

Sample Output

Finance : 73000
HR : 83000
IT : 127000

Technologies Used

Python 3

Visual Studio Code (VS Code)


Files Description

splitter.py – Splits the input file into two chunks.

mapper.py – Extracts Department and Salary as key-value pairs.

partitioner.py – Sends data to reducers using hash(key) % 2.

sorter.py – Sorts the partitioned data.

reducer.py – Calculates the total salary for each department.

master.py – Executes the complete MapReduce workflow.

