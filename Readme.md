<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F0C29,50:302B63,100:A855F7&height=220&section=header&text=Data%20Structures%20in%20Python&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Clean%20%7C%20Documented%20%7C%20Beginner-Friendly%20Implementations&descAlignY=55&descSize=16" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=3000&pause=1000&color=A855F7&center=true&vCenter=true&width=600&lines=Array+%7C+Linked+List+%7C+Stack+%7C+Queue;Hashing+%7C+Trees+%7C+and+more...;Every+DS+implemented+from+scratch+in+Python!" alt="Typing SVG" />

<div align="center">

<!-- Animated Typing SVG -->
<a href="https://github.com/Suman18-bit/Data-Structure-in-Python">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=28&pause=1000&color=F75000&center=true&vCenter=true&random=false&width=600&height=50&lines=Data+Structures+in+Python;Algorithms+%7C+OOP+%7C+Efficiency;Code+%E2%9A%A1+Learn+%E2%9A%A1+Grow" alt="Typing SVG" />
</a>

<!-- Dynamic Badges -->
<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Code-Quality-A%2B-brightgreen?style=for-the-badge&logo=github" alt="Quality">
  <img src="https://img.shields.io/github/license/Suman18-bit/Data-Structure-in-Python?style=for-the-badge&color=blue" alt="License">
  <img src="https://img.shields.io/github/last-commit/Suman18-bit/Data-Structure-in-Python?style=for-the-badge&color=orange" alt="Last Commit">
</p>

<!-- Wave Animation -->
<img src="https://raw.githubusercontent.com/ABSphreak/ABSphreak/master/gifs/Hi.gif" width="30px" height="30px"> 
<br>
<i>A highly visual, well-documented collection of fundamental data structures implemented purely in Python.</i>

<br>
<hr style="border: 1px solid #3776AB; border-radius: 5px;">

</div>

## 🎯 Why this Repository?

> 💡 **"Choose the right data structure, and 90% of your algorithmic problems solve themselves."**

Whether you are a CS student preparing for finals, a developer grinding LeetCode, or just someone curious about how things work under the hood—this repo provides clean, PEP-8 compliant, and heavily commented implementations of the most essential data structures.

---

## 🚀 Implemented Data Structures (Interactive)

<details>
  <summary><b>🟦 1. Arrays (Click to Expand)</b></summary>
  
  <br>
  
  > A collection of items stored at contiguous memory locations. 
  
  **Visualizing the Array:**
  ```text
  Index:   0    1    2    3    4
        +----+----+----+----+----+
  Data  | 10 | 20 | 30 | 40 | 50 |
        +----+----+----+----+----+
  ```
  **Included Implementations:**
  - [x] Dynamic Array Resizing
  - [x] Searching & Sorting Algorithms
  - [x] Array Rotations & Manipulations
  
</details>

<details>
  <summary><b>🔗 2. Linked Lists (Click to Expand)</b></summary>
  
  <br>
  
  > A linear data structure where elements are not stored at contiguous locations, but linked using pointers.
  
  **Visualizing the Linked List:**
  ```text
  HEAD                                          TAIL
    |                                             |
    v                                             v
  +----+------+     +----+------+     +----+------+
  | 10 | next |---->| 20 | next |---->| 30 | NULL |
  +----+------+     +----+------+     +----+------+
  ```
  **Included Implementations:**
  - [x] Singly Linked List (Insert, Delete, Search)
  - [x] Doubly Linked List
  - [x] Cycle Detection (Floyd’s Tortoise and Hare)
  
</details>

<details>
  <summary><b>🌳 3. Trees & Traversals (Click to Expand)</b></summary>
  
  <br>
  
  > A hierarchical data structure consisting of nodes connected by edges.
  
  **Visualizing the Binary Tree:**
  ```text
          1           <-- Root
        /   \
       2     3        <-- Children of 1
      / \   / \
     4   5 6   7       <-- Leaf Nodes
  ```
  **Included Implementations:**
  - [x] Binary Search Tree (BST) Insertion
  - [x] In-Order, Pre-Order, Post-Order (DFS)
  - [x] Level-Order Traversal (BFS)
  
</details>

<details>
  <summary><b>#️⃣ 4. Hashing (Click to Expand)</b></summary>
  
  <br>
  
  > A technique that maps keys to values using a hash function for O(1) average time complexity.
  
  **Visualizing the Hash Table:**
  ```text
  [ Key: "apple" ] --hash()--> [ Index: 4 ] --> [ Bucket: "A red fruit" ]
  ```
  **Included Implementations:**
  - [x] Custom Hash Table class
  - [x] Collision Resolution (Chaining)
  - [x] Open Addressing concepts
  
</details>

---

## 📂 Project Architecture

```text
📁 Data-Structure--in--Python/
│
├── 📁 .github/             # CI/CD Workflows & GitHub Actions
├── 📁 Array/               # Arrays & dynamic resizing
├── 📁 Hashing/             # Hash tables & collision handling
├── 📁 Linked_List/         # Singly & Doubly Linked Lists
├── 📁 Tree/                # Binary Trees & BST traversals
│
├── 📄 LICENSE              # MIT License
└── 📄 Readme.md            # You are here ✨
```

---

## ⚙️ Quick Start Guide

Getting this running locally is as easy as 1-2-3!

**Step 1: Clone the repository**
```bash
git clone https://github.com/Suman18-bit/Data-Structure--in--Python.git
```

**Step 2: Navigate to the directory**
```bash
cd Data-Structure--in--Python
```

**Step 3: Run a module**
```bash
python Tree/binary_tree.py
```

> 🛠️ **Prerequisite:** Requires Python 3.8 or higher. No external dependencies required!

---

## 🤝 Contributing

Contributions, issues, and feature requests are what make the open-source community an amazing place to learn, inspire, and create. **Any contributions you make are greatly appreciated.**

1. 🍴 Fork the Project
2. 🌿 Create your Feature Branch (`git checkout -b feature/NewDataStructure`)
3. 💻 Commit your Changes (`git commit -m 'Add some NewDataStructure'`)
4. 🚀 Push to the Branch (`git push origin feature/NewDataStructure`)
5. 📝 Open a Pull Request

---

<div align="center">

### 📜 License
Distributed under the **MIT License**. See `LICENSE` for more information.

### 💖 Support & Acknowledgements
If you found this repository helpful, please consider giving it a star! ⭐
<br><br>
<img src="https://img.shields.io/github/stars/Suman18-bit/Data-Structure-in-Python?style=social" alt="Stars">
<br><br>
<b>Built with 💻 and ☕ by <a href="https://github.com/Suman18-bit">Suman18-bit</a></b>

<!-- Footer Animation -->
<img src="https://raw.githubusercontent.com/trinib/trinib/main/.images/wave.gif" width="100px" height="100px">

</div>
