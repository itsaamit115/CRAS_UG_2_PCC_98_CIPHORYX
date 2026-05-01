# 🖥️ Campus Resource Allocation System (CRAS)
![C](https://img.shields.io/badge/C-Backend-blue)
![Python](https://img.shields.io/badge/Python-Frontend-green)
![GUI](https://img.shields.io/badge/GUI-CustomTkinter-orange)
![Status](https://img.shields.io/badge/Project-Academic-success)

A **simple, efficient, and practical resource management system** that allows users to **add, allocate, release, and manage resources** using a combination of **C backend and Python GUI frontend**.


## ✨ Project Highlights

- 🔄 Full CRUD operations on resources
- 🧠 Backend logic written in C (high performance)
- 🖥️ Modern GUI using CustomTkinter (Python)
- 📄 Automatic PDF report generation
- 📂 File-based database system (.dat files)
- 🚀 Perfect for college projects & system design understanding


## 📁 Project Structure

---
CRAS-System/
│
├── back_end.c
├── back_end.exe
├── cras.h
│
├── fornt_end.py
├── logo.ico
│
├── input.txt
├── output.txt
├── source.dat
├── inuse.dat
│
└── Resource_Report.pdf
---



## 🔧 Core Features

### 🔹 Resource Management

- Add new resources  
- View all resources  
- Delete resources (only if not allocated)  


### 🔹 Allocation System

- Allocate resource to Student / Faculty
- Release resources
- Prevent double allocation


### 🔹 File Handling System

- Uses .dat files as database:
  - source.dat → stores all resources
  - inuse.dat → stores allocated resources  


### 🔹 GUI Interface (Python)

- Clean modern UI using CustomTkinter
- Dropdown-based selection for available resources
- Popup-based feedback system



### 🔹 PDF Report Generation

- Converts resource table into PDF format
- Uses reportlab library



## ▶️ How to Run

### Step 1: Install Python Libraries
```
pip install customtkinter reportlab pillow
```

### Step 2: Compile Backend
```
gcc back_end.c -o back_end.exe
```

### Step 3: Run Frontend
```
python fornt_end.py
```



## 🧠 Working Flow

1. User interacts with GUI  
2. GUI writes command into input.txt  
3. Backend processes it  
4. Output saved in output.txt  
5. GUI reads and displays result  



## 🎯 Learning Outcomes

- File handling in C  
- Struct-based data management  
- GUI development with Python  
- Backend–Frontend integration  
- Real-world system design thinking  



## 🚀 Use Cases

- College Mini Project  
- Resume Project  
- Learning File-Based DB Systems  



## 👨‍💻 Authors

- Amit Singh  
- Sarthak Singh  
- Krishna Uniyal  



⭐ Star the repo if you like it!
