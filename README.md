<!-- ============ HEADER ============ -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=220&section=header&text=UPES%20100%20Days%20of%20Code&fontSize=44&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=B.Tech%20CSE%20%C2%B7%20UPES%20Dehradun&descAlignY=58&descSize=18" alt="header" />

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=36BCF7&center=true&vCenter=true&width=600&lines=Code+every+day.+No+excuses.;Consistency+beats+intensity.;Committing+Day+by+Day+%F0%9F%9A%80;Learning+C.+Building+habits." alt="Typing SVG" />
</a>

<br/>

![Days Completed](https://img.shields.io/badge/Days_Completed-43%2F100-36BCF7?style=for-the-badge&logo=target&logoColor=white)
![Language](https://img.shields.io/badge/Language-C-00599C?style=for-the-badge&logo=c&logoColor=white)
![Status](https://img.shields.io/badge/Status-In_Progress-brightgreen?style=for-the-badge)
![Commits](https://img.shields.io/github/commit-activity/t/paarthmishra-git/PAARTHMISHRA-UPES-100DAYSCODING?style=for-the-badge&color=orange)
![Last Commit](https://img.shields.io/github/last-commit/paarthmishra-git/PAARTHMISHRA-UPES-100DAYSCODING?style=for-the-badge&color=purple)

**[About](#-about) · [Progress](#-progress-tracker) · [Day Log](#-day-log) · [Stack](#-tech-stack) · [Stats](#-github-stats) · [Run It](#-run-any-program) · [Connect](#-connect)**

</div>

---

## 🎯 About

A **100-day coding challenge** from my B.Tech in Computer Science and Engineering at **UPES Dehradun**. The goal is simple: build a daily coding habit, sharpen problem-solving, and document everything publicly.

<table>
<tr>
<td width="33%" valign="top">

### 🔥 Objectives
- Code **100 days** in a row
- Master programming fundamentals
- Build and document in public

</td>
<td width="33%" valign="top">

### 📏 Rules
- Minimum **1 hour** per day
- One commit for every day
- No skipped days

</td>
<td width="33%" valign="top">

### 🧠 Focus Areas
- Problem solving
- Strings and arrays
- Clean, commented code

</td>
</tr>
</table>

---

## 📈 Progress Tracker

```text
Day 43 of 100
▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱  43%
```

### 🏁 Milestones

- [x] 🌱 **Day 1** – Started the challenge
- [x] 🔟 **Day 10** – First 10 days done
- [x] 2️⃣5️⃣ **Day 25** – Quarter of the way
- [ ] 5️⃣0️⃣ **Day 50** – Halfway point
- [ ] 7️⃣5️⃣ **Day 75** – Final stretch
- [ ] 💯 **Day 100** – Challenge complete

---

## 📅 Day Log

> Click a block to expand it. 👇

<details>
<summary><b>🟢 Days 41 – 43 · Strings (latest)</b></summary>
<br/>

| Day | Program | Concept |
|:---:|:--------|:--------|
| 43 | [`day43q1.c`](./day43q1.c) | Count spaces, digits and special characters in a string |
| 43 | [`day43q2.c`](./day43q2.c) | String practice |
| 42 | [`day42q1.c`](./day42q1.c) · [`day42q2.c`](./day42q2.c) | String practice |
| 41 | [`day41a.c`](./day41a.c) · [`day41b.c`](./day41b.c) · [`day41c.c`](./day41c.c) | String practice |
| 41 | [`day41q1.c`](./day41q1.c) · [`day41q2.c`](./day41q2.c) | String practice |

</details>

<details>
<summary><b>🔵 Days 31 – 40</b></summary>
<br/>

| Day | Program | Concept |
|:---:|:--------|:--------|
| 40 | [`day40q2.c`](./day40q2.c) | _add topic_ |
| … | … | … |

</details>

<details>
<summary><b>🟣 Days 1 – 30</b></summary>
<br/>

| Day | Program | Concept |
|:---:|:--------|:--------|
| 7 | [`day7q1.c`](./day7q1.c) · [`day7q2.c`](./day7q2.c) | _add topic_ |
| 6 | [`day6q1.c`](./day6q1.c) · [`day6q2.c`](./day6q2.c) | _add topic_ |
| 5 | [`day5q1.c`](./day5q1.c) · [`day5q2.c`](./day5q2.c) | _add topic_ |
| 4 | [`day4q1.c`](./day4q1.c) · [`day4q2.c`](./day4q2.c) | _add topic_ |
| … | … | … |

</details>

<details>
<summary><b>💡 Featured snippet: Day 43 (character counter)</b></summary>

```c
//Count the number of spaces, digits, and special characters in a string.
#include <stdio.h>
#include <ctype.h>

int main() {
    char str[100];
    int spaces = 0, digits = 0, special = 0;

    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);

    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] == '\n' || str[i] == '\r') {
            continue;  // ignore newline from fgets
        }

        if (str[i] == ' ') {
            spaces++;
        } else if (isdigit((unsigned char)str[i])) {
            digits++;
        } else if (!isalpha((unsigned char)str[i])) {
            special++;
        }
    }

    printf("Spaces: %d\n", spaces);
    printf("Digits: %d\n", digits);
    printf("Special characters: %d\n", special);
    return 0;
}
```

</details>

---

## 🛠 Tech Stack

<div align="center">

![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)

</div>

---

## 📊 GitHub Stats

<div align="center">

<img height="170" src="https://github-readme-stats.vercel.app/api?username=paarthmishra-git&show_icons=true&theme=tokyonight&hide_border=true" alt="stats" />
<img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=paarthmishra-git&layout=compact&theme=tokyonight&hide_border=true" alt="top languages" />

<br/>

<img src="https://streak-stats.demolab.com?user=paarthmishra-git&theme=tokyonight&hide_border=true" alt="streak" />

<br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=paarthmishra-git&theme=tokyo-night&hide_border=true" alt="activity graph" />

</div>

---

## ▶️ Run Any Program

<details>
<summary><b>Click for compile-and-run steps</b></summary>

```bash
# 1. Clone the repo
git clone https://github.com/paarthmishra-git/PAARTHMISHRA-UPES-100DAYSCODING.git
cd PAARTHMISHRA-UPES-100DAYSCODING

# 2. Compile any file
gcc day43q1.c -o day43q1

# 3. Run it
./day43q1          # Linux / macOS
day43q1.exe        # Windows
```

</details>

<details>
<summary><b>📝 File naming convention</b></summary>

`day<N>q<M>.c` means Day **N**, Question **M**. For example, `day43q1.c` is Day 43, Question 1.

</details>

---

## 🤝 Connect

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-paarthmishra--git-181717?style=for-the-badge&logo=github)](https://github.com/paarthmishra-git)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-your--name-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/your-profile)

<br/>

⭐ **If this repo motivates you, drop a star and start your own 100-day streak!** ⭐

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,100:0f2027&height=100&section=footer" alt="footer" />

</div>
