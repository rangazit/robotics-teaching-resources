# Online resources for teaching robotics and autonomous systems

A curated, checked list of courses, textbooks, videos, exercises and software for teaching an introductory university course on robotics and autonomous systems.

**Interactive version** (filters, search, connections between resources): https://rangazit.github.io/robotics-teaching-resources/

*Free online* lists the materials that are freely available for each resource; open the details under each table for the source of every item and for paid or partial materials. A course offered in several ways (for example a university course and its MOOC) is listed once; the other ways are in the last column.

## Contents

- [University courses](#university-courses)
- [MOOCs and short online courses](#moocs-and-short-online-courses)
- [Textbooks](#textbooks)
- [Video lecture series](#video-lecture-series)
- [Labs, exercises and notebooks](#labs-exercises-and-notebooks)
- [Robot learning, physical AI and embodied AI](#robot-learning-physical-ai-and-embodied-ai)
- [Simulators and software for teaching](#simulators-and-software-for-teaching)
- [Which course uses which book and software](#which-course-uses-which-book-and-software)
- [How to contribute](#how-to-contribute)

## University courses

Courses with public lecture material (slides, notes, videos or assignments).

| Resource | Free online | Textbook | Software | Other ways to take it |
|---|---|---|---|---|
| **[Autonomous Mobile Robots](https://asl.ethz.ch/education/lectures/autonomous_mobile_robots/spring-2021.html)**<br><sub>ETH Zurich (Autonomous Systems Lab), 2021</sub> | slides, video, exercises, solutions, code | [Siegwart et al.](https://bookshop.org/p/books/introduction-to-autonomous-mobile-robots-second-edition-davide-scaramuzza/a2f4851c1824469c) | CoppeliaSim, MATLAB | [ETH lecture page, spring 2020](https://asl.ethz.ch/education/lectures/autonomous_mobile_robots/spring-2020.html)<br>[edX MOOC AMRx (self-paced)](https://www.edx.org/learn/autonomous-robotics/eth-zurich-autonomous-mobile-robots) |
| **[Principles of Robot Autonomy I (AA 174A / AA 274A)](https://stanfordasl.github.io/PoRA-I/aa174a_aut2526/)**<br><sub>Stanford University (Autonomous Systems Lab), 2025</sub> | slides, notes<br><sub>partly: video, exercises, solutions, code</sub> |  | ROS 2 | [AA 274A, autumn 2025](https://stanfordasl.github.io/PoRA-I/aa274a_aut2526)<br>[AA 174A, autumn 2024 (slides, notes, notebooks)](https://stanfordasl.github.io/PoRA-I/aa174a_aut2425) |
| **[Introduction to Robotics (CS 223A)](https://see.stanford.edu/Course/CS223A)**<br><sub>Stanford University, 2008</sub> | notes, video, exercises | [Siciliano et al.](https://link.springer.com/book/10.1007/978-1-84628-642-1) |  | [Current course page (winter 2026, materials on Canvas)](https://cs.stanford.edu/groups/manips/teaching/cs223a) |
| **[Introduction to Robotics and Perception (CS 3630)](https://dellaert.github.io/25F-3630/schedule.html)**<br><sub>Georgia Tech, 2025</sub> | book, slides, notes, code<br><sub>partly: exercises</sub> | [Dellaert & Hutchinson](https://www.roboticsbook.org/intro.html) | GTSAM | [Fall 2022 site](https://dellaert.github.io/22F-3630/schedule.html) |
| **[Introduction to Robotics (CSCI 3302)](https://introduction-to-autonomous-robots.github.io/csci3302.html)**<br><sub>University of Colorado Boulder, 2022</sub> | book, notes, video<br><sub>partly: code</sub> | [Correll et al.](https://introduction-to-autonomous-robots.github.io) | Webots | [Coursera specialization 'Introduction to Robotics with Webots' (3 courses)](https://www.coursera.org/specializations/introduction-robotics-webots)<br>[YouTube lecture playlist](https://www.youtube.com/playlist?list=PLJafQ8U0gQVXVSg9_AjS1ZhT2E0FbPy2F) |
| **[Introduction to Robotics (Hanze)](https://drive.google.com/drive/folders/1JfLwLR_FMLuedeSI55oBdiNAt0H76jtr?usp=sharing)**<br><sub>Hanze University of Applied Sciences, 2024</sub> | book, slides, exercises, code | [Elements of Robotics](https://link.springer.com/book/10.1007/978-3-319-62533-1) | Webots | [Robotics Simulation Labs](https://felipenmartins.github.io/Robotics-Simulation-Labs/) |
| **[Introduction to Robotics (MAE 345 / ECE 345 / COS 346)](https://irom-lab.princeton.edu/intro-to-robotics/)**<br><sub>Princeton University, 2026</sub> | slides, notes, exercises, code<br><sub>partly: video</sub> |  | Crazyflie | [YouTube lecture videos (2026, posted weekly)](https://www.youtube.com/@intro-to-robotics)<br>[Assignments on GitHub](https://github.com/Princeton-Introduction-to-Robotics) |
| **[Robotic Manipulation (6.4210 / 6.4212)](https://manipulation.csail.mit.edu/Fall2025/)**<br><sub>MIT, 2025</sub> | book, notes, video, exercises, code | [Robotic Manipulation (book)](https://manipulation.mit.edu) | Drake | [MIT OpenCourseWare, fall 2022 (lecture videos)](https://ocw.mit.edu/courses/6-4210-robotic-manipulation-fall-2022) |
| **[Underactuated Robotics (6.832)](https://underactuated.mit.edu/)**<br><sub>MIT, 2024</sub> | book, notes, video, exercises, code | [Underactuated Robotics (book)](https://underactuated.mit.edu/) | Drake |  |
| **[Mobile Robot Algorithms Laboratory (16-362)](https://mral-cmu.github.io)**<br><sub>Carnegie Mellon University, 2026</sub> | slides<br><sub>partly: exercises, code</sub> |  | Python |  |
| **[Introduction to Robotics (16-311)](https://www.cs.cmu.edu/~16311/s25/schedule/scheduleindex.html)**<br><sub>Carnegie Mellon University, 2025</sub> | exercises<br><sub>partly: slides, notes</sub> |  |  |  |
| **[Self-Driving Cars with Duckietown](https://duckietown.com/mooc/)**<br><sub>ETH Zurich, Université de Montréal, TTIC (Duckietown), 2025</sub> | notes, video, exercises, code |  | ROS 1 | [Instructor manual and curricula](https://docs.duckietown.com/ente/instructor-manual/curricula/mooc/index.html) |

<details><summary>Details: offerings, sources of each material, notes</summary>

**Autonomous Mobile Robots** — R. Siegwart, M. Chli, M. Hutter, D. Scaramuzza, P. Furgale, M. Rufli et al. (ETH Zurich (Autonomous Systems Lab))

- Offering: [ETH lecture page, spring 2021](https://asl.ethz.ch/education/lectures/autonomous_mobile_robots/spring-2021.html) — free
- Offering: [ETH lecture page, spring 2020](https://asl.ethz.ch/education/lectures/autonomous_mobile_robots/spring-2020.html) — free
- Offering: [edX MOOC AMRx (self-paced)](https://www.edx.org/learn/autonomous-robotics/eth-zurich-autonomous-mobile-robots) — free-audit
- Materials: Book: paid (Siegwart, Nourbakhsh, Scaramuzza (2011)); Slides: free (ETH 2020 and 2021 pages; edX); Notes: not available; Video: free (edX MOOC); Exercises: free (ETH 2021 page (6 exercises)); Solutions: free (ETH 2021 page); Code: free (exercise templates)
- Textbook: Introduction to Autonomous Mobile Robots (2nd ed.)
- The classic mobile-robotics course: locomotion, kinematics, perception, line extraction, Markov and Kalman localization, EKF SLAM, planning. The exercises use CoppeliaSim with MATLAB. Slides are dense but complete.

**Principles of Robot Autonomy I (AA 174A / AA 274A)** — M. Pavone, M. Schwager (Stanford University (Autonomous Systems Lab))

- Offering: [AA 174A, autumn 2025](https://stanfordasl.github.io/PoRA-I/aa174a_aut2526/) — free
- Offering: [AA 274A, autumn 2025](https://stanfordasl.github.io/PoRA-I/aa274a_aut2526) — free
- Offering: [AA 174A, autumn 2024 (slides, notes, notebooks)](https://stanfordasl.github.io/PoRA-I/aa174a_aut2425) — free
- Materials: Book: not available; Slides: free (course sites (all lectures)); Notes: free (2024 site (course notes PDF)); Video: partial (a few recordings; the rest on Canvas); Exercises: partial (homework pages of past years); Solutions: partial (practice exam solutions only); Code: partial (Jupyter notebooks, ROS 2 setup guide)
- Very clear slides with consistent notation (Thrun et al.): state estimation, Bayes, Kalman and particle filters, EKF localization, SLAM, planning, trajectory optimization and tracking, perception. Labs on TurtleBot with ROS 2.

**Introduction to Robotics (CS 223A)** — O. Khatib (Stanford University)

- Offering: [Stanford Engineering Everywhere (2008 recording)](https://see.stanford.edu/Course/CS223A) — free
- Offering: [Current course page (winter 2026, materials on Canvas)](https://cs.stanford.edu/groups/manips/teaching/cs223a) — free
- Materials: Book: paid (course reader; Siciliano et al. as supplement); Slides: not available; Notes: free (SEE handouts and lecture transcripts); Video: free (SEE (16 lectures)); Exercises: free (SEE (6 problem sets)); Solutions: not available; Code: not available
- Textbook: Robotics: Modelling, Planning and Control
- Manipulator kinematics, Jacobians, dynamics and control. Older recordings, but a complete classic course.

**Introduction to Robotics and Perception (CS 3630)** — F. Dellaert, S. Hutchinson (Georgia Tech)

- Offering: [Fall 2025 site (schedule with slides)](https://dellaert.github.io/25F-3630/schedule.html) — free
- Offering: [Fall 2022 site](https://dellaert.github.io/22F-3630/schedule.html) — free
- Materials: Book: free (roboticsbook.org (online, interactive)); Slides: free (fall 2025 schedule); Notes: free (the book); Video: not available (Canvas only); Exercises: partial (project descriptions on the course site); Solutions: not available; Code: free (book notebooks (BSD-3))
- Textbook: Introduction to Robotics and Perception
- Built around six running examples (sorter, vacuum, warehouse, differential drive, car, drone). Each covers state, actions, sensing, perception, planning and learning, in Python notebooks.

**Introduction to Robotics (CSCI 3302)** — N. Correll, B. Hayes, A. Roncone (University of Colorado Boulder)

- Offering: [Course page](https://introduction-to-autonomous-robots.github.io/csci3302.html) — free
- Offering: [Coursera specialization 'Introduction to Robotics with Webots' (3 courses)](https://www.coursera.org/specializations/introduction-robotics-webots) — paid
- Offering: [YouTube lecture playlist](https://www.youtube.com/playlist?list=PLJafQ8U0gQVXVSg9_AjS1ZhT2E0FbPy2F) — free
- Materials: Book: free (Correll et al. (source on GitHub)); Slides: unknown; Notes: free (the book); Video: free (YouTube playlist; Coursera); Exercises: paid (Coursera (peer-graded Webots projects)); Solutions: not available; Code: partial (Webots worlds in the Coursera course)
- Textbook: Introduction to Autonomous Robots
- Low-level introduction built on Webots: odometry, forward and inverse kinematics, mapping, planning, behaviour trees and a mobile-manipulation project.

**Introduction to Robotics (Hanze)** — F. N. Martins (Hanze University of Applied Sciences)

- Offering: [Lecture slides (Google Drive)](https://drive.google.com/drive/folders/1JfLwLR_FMLuedeSI55oBdiNAt0H76jtr?usp=sharing) — free
- Offering: [Robotics Simulation Labs](https://felipenmartins.github.io/Robotics-Simulation-Labs/) — free
- Materials: Book: free (Elements of Robotics (open access)); Slides: free (Google Drive folder); Notes: not available; Video: not available; Exercises: free (9 Webots labs (MIT license)); Solutions: not available; Code: free (lab templates on GitHub)
- Textbook: Elements of Robotics · Built for: Introduction to Robotics (CSCI 3302)
- Clear, well-designed slides and step-by-step Webots labs: state machines, line following, odometry, PID go-to-goal, trajectory tracking, Dijkstra.

**Introduction to Robotics (MAE 345 / ECE 345 / COS 346)** — A. Majumdar (Princeton University)

- Offering: [Course site (slides, notes, assignments)](https://irom-lab.princeton.edu/intro-to-robotics/) — free
- Offering: [YouTube lecture videos (2026, posted weekly)](https://www.youtube.com/@intro-to-robotics) — free
- Offering: [Assignments on GitHub](https://github.com/Princeton-Introduction-to-Robotics) — free
- Materials: Book: not available; Slides: free (course site); Notes: free (course site); Video: partial (YouTube (being posted during the fall 2026 term)); Exercises: free (course site and GitHub); Solutions: not available; Code: free (GitHub)
- Hands-on course with Crazyflie mini drones; covers feedback control, vision, motion planning and learning.

**Robotic Manipulation (6.4210 / 6.4212)** — R. Tedrake, T. Lozano-Pérez (MIT)

- Offering: [Course site, fall 2025](https://manipulation.csail.mit.edu/Fall2025/) — free
- Offering: [MIT OpenCourseWare, fall 2022 (lecture videos)](https://ocw.mit.edu/courses/6-4210-robotic-manipulation-fall-2022) — free
- Materials: Book: free (online textbook (manipulation.mit.edu)); Slides: unknown; Notes: free (online textbook); Video: free (MIT OCW (2022)); Exercises: free (problem sets on the course site); Solutions: not available; Code: free (Drake notebooks in the textbook)
- Textbook: Robotic Manipulation: Perception, Planning, and Control
- Perception, planning and control for robot arms, with runnable Drake examples in every chapter.

**Underactuated Robotics (6.832)** — R. Tedrake (MIT)

- Offering: [Online notes and course](https://underactuated.mit.edu/) — free
- Materials: Book: free (online notes (HTML and PDF)); Slides: not available; Notes: free (online notes); Video: free (YouTube); Exercises: free (end-of-chapter exercises); Solutions: not available; Code: free (Drake / Colab notebooks)
- Textbook: Underactuated Robotics: Algorithms for Walking, Running, Swimming, Flying, and Manipulation
- Nonlinear dynamics and control of walking, flying and swimming robots; optimisation-based control.

**Mobile Robot Algorithms Laboratory (16-362)** — W. Tabib (Carnegie Mellon University)

- Offering: [Course site, fall 2026](https://mral-cmu.github.io) — free
- Materials: Book: not available; Slides: free (posted with each lecture); Notes: not available; Video: not available; Exercises: partial (assignments distributed through GitHub); Solutions: not available; Code: partial
- Quadrotor autonomy from scratch in Python. Dynamics simulation, control, mapping, estimation, planning, exploration.

**Introduction to Robotics (16-311)** — H. Choset (Carnegie Mellon University)

- Offering: [Course site, spring 2025](https://www.cs.cmu.edu/~16311/s25/schedule/scheduleindex.html) — free
- Materials: Book: not available; Slides: partial (lecture notes linked as they are released); Notes: partial; Video: not available; Exercises: free (homework PDFs); Solutions: not available; Code: not available
- Undergraduate introduction with hardware labs; homework handouts are public.

**Self-Driving Cars with Duckietown** — A. Censi, L. Paull, J. Tani, M. Walter et al. (ETH Zurich, Université de Montréal, TTIC (Duckietown))

- Offering: [edX MOOC (2025 edition, with virtual Duckiebots)](https://duckietown.com/mooc/) — free
- Offering: [Instructor manual and curricula](https://docs.duckietown.com/ente/instructor-manual/curricula/mooc/index.html) — free
- Materials: Book: not available; Slides: unknown; Notes: free (Duckietown documentation); Video: free (edX MOOC; YouTube preview); Exercises: free (exercises in simulation, on virtual or real Duckiebots); Solutions: not available; Code: free (open-source Duckietown stack)
- Hands-on autonomous driving with small robots; hardware optional since 2025 (virtual Duckiebots).

</details>

## MOOCs and short online courses

Self-paced online courses that are not part of a university course listed above.

| Resource | Free online | Textbook | Software | Other ways to take it |
|---|---|---|---|---|
| **[Modern Robotics](https://hades.mech.northwestern.edu/index.php/Modern_Robotics)**<br><sub>Northwestern University, 2017</sub> | book, notes, video, exercises, code<br><sub>partly: solutions</sub> | [Modern Robotics (book)](https://hades.mech.northwestern.edu/index.php/Modern_Robotics) | CoppeliaSim, MATLAB | [Coursera specialization (6 courses)](https://www.coursera.org/specializations/modernrobotics) |
| **[Self-Driving Cars Specialization](https://www.coursera.org/specializations/self-driving-cars)**<br><sub>University of Toronto (Coursera), 2019</sub> | — |  | CARLA |  |
| **[Robotics Specialization](https://www.coursera.org/learn/robotics-flight)**<br><sub>University of Pennsylvania (Coursera), 2016</sub> | video |  | MATLAB | [Class Central overview of the specialization](https://classcentral.com/course/robotics-18626) |
| **[A Beginner's Guide to Autonomous Robots](https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-OV-35+V1)**<br><sub>NVIDIA Deep Learning Institute</sub> | video |  |  |  |
| **[AI for Autonomous Vehicles and Robotics](https://www.coursera.org/learn/ai-for-autonomous-vehicles-and-robotics)**<br><sub>University of Michigan (Coursera)</sub> | video |  |  |  |
| **[Artificial Intelligence for Robotics](https://www.coursera.org/learn/packt-artificial-intelligence-for-robotics)**<br><sub>Packt (Coursera)</sub> | — |  | ROS 2 |  |

<details><summary>Details: offerings, sources of each material, notes</summary>

**Modern Robotics** — K. M. Lynch, F. C. Park (Northwestern University)

- Offering: [Book, videos and software (Northwestern wiki)](https://hades.mech.northwestern.edu/index.php/Modern_Robotics) — free
- Offering: [Coursera specialization (6 courses)](https://www.coursera.org/specializations/modernrobotics) — free-audit
- Materials: Book: free (preprint PDF (several formats)); Slides: not available; Notes: free (the book); Video: free (book site and YouTube); Exercises: free (book exercises; Coursera assignments); Solutions: partial (Coursera graded assignments); Code: free (Python, MATLAB and Mathematica library)
- Textbook: Modern Robotics: Mechanics, Planning, and Control
- Screw theory and product of exponentials; a full course in short videos with a free book.

**Self-Driving Cars Specialization** — S. Waslander, J. Kelly (University of Toronto (Coursera))

- Offering: [Coursera specialization (4 courses)](https://www.coursera.org/specializations/self-driving-cars) — paid
- Materials: Book: not available; Slides: not available; Notes: not available; Video: paid (Coursera); Exercises: paid (Coursera projects in CARLA); Solutions: not available; Code: paid
- State estimation (EKF, ES-EKF), visual perception and motion planning for cars; projects in CARLA.

**Robotics Specialization** — V. Kumar, D. Lee, K. Daniilidis, C. J. Taylor, J. Shi, D. Koditschek (University of Pennsylvania (Coursera))

- Offering: [Coursera: Aerial Robotics (first of 6 courses)](https://www.coursera.org/learn/robotics-flight) — free-audit
- Offering: [Class Central overview of the specialization](https://classcentral.com/course/robotics-18626) — free
- Materials: Book: not available; Slides: not available; Notes: not available; Video: free (Coursera (audit)); Exercises: paid (Coursera graded assignments); Solutions: not available; Code: paid
- Aerial robotics, computational motion planning, mobility, perception, estimation and learning; MATLAB assignments.

**A Beginner's Guide to Autonomous Robots** —  (NVIDIA Deep Learning Institute)

- Offering: [NVIDIA DLI (about 1 hour)](https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-OV-35+V1) — free
- Materials: Book: not available; Slides: not available; Notes: not available; Video: free; Exercises: not available; Solutions: not available; Code: not available
- One-hour overview of an autonomous-robot software stack; good as a first motivating lecture.

**AI for Autonomous Vehicles and Robotics** —  (University of Michigan (Coursera))

- Offering: [Coursera course (about 1 week)](https://www.coursera.org/learn/ai-for-autonomous-vehicles-and-robotics) — free-audit
- Materials: Book: not available; Slides: not available; Notes: not available; Video: free (Coursera (audit)); Exercises: paid; Solutions: not available; Code: not available
- Short overview of machine learning for perception and decision making; not at university-course depth.

**Artificial Intelligence for Robotics** —  (Packt (Coursera))

- Offering: [Coursera course (about 2 weeks)](https://www.coursera.org/learn/packt-artificial-intelligence-for-robotics) — paid
- Materials: Book: not available; Slides: not available; Notes: not available; Video: paid; Exercises: paid; Solutions: not available; Code: paid
- Applied project course (object recognition, RL, navigation) with ROS 2 and OpenCV.

</details>

## Textbooks

Textbooks used by the courses above, and other free or open textbooks.

| Resource | Free online | Textbook | Software | Other ways to take it |
|---|---|---|---|---|
| **[Introduction to Autonomous Mobile Robots (2nd ed.)](https://bookshop.org/p/books/introduction-to-autonomous-mobile-robots-second-edition-davide-scaramuzza/a2f4851c1824469c)**<br><sub>MIT Press, 2011</sub> | — |  |  |  |
| **[Introduction to Autonomous Robots](https://introduction-to-autonomous-robots.github.io)**<br><sub>MIT Press / open source, 2022</sub> | book |  |  | [Source and releases on GitHub](https://github.com/Introduction-to-Autonomous-Robots/Introduction-to-Autonomous-Robots/releases)<br>[Open Textbook Library](https://open.umn.edu/opentextbooks/textbooks/316) |
| **[Robotics, Vision and Control: Fundamental Algorithms in Python (3rd ed.)](https://petercorke.com/rvc3p/home/)**<br><sub>Springer, 2023</sub> | code |  | Robotics Toolbox (Python) | [Springer](https://link.springer.com/book/10.1007/978-3-031-06469-2)<br>[Code and notebooks for every chapter](https://github.com/petercorke/RVC3-python) |
| **[Introduction to Robotics and Perception](https://www.roboticsbook.org/intro.html)**<br><sub>Georgia Tech (online, draft), 2024</sub> | book, code |  | GTSAM | [Notebooks on GitHub](https://github.com/gtbook/robotics) |
| **[Elements of Robotics](https://link.springer.com/book/10.1007/978-3-319-62533-1)**<br><sub>Springer (open access), 2018</sub> | book |  |  |  |
| **[Modern Robotics: Mechanics, Planning, and Control](https://hades.mech.northwestern.edu/index.php/Modern_Robotics)**<br><sub>Cambridge University Press, 2017</sub> | book, video, code |  |  |  |
| **[Probabilistic Robotics](https://robots.stanford.edu/probabilistic-robotics/)**<br><sub>MIT Press, 2005</sub> | — |  |  |  |
| **[State Estimation for Robotics (2nd ed.)](https://asrl.utias.utoronto.ca/~tdb/)**<br><sub>Cambridge University Press, 2024</sub> | book |  |  |  |
| **[Planning Algorithms](https://lavalle.pl/planning/)**<br><sub>Cambridge University Press, 2006</sub> | book |  |  |  |
| **[Robotic Systems (draft)](https://motion.cs.illinois.edu/RoboticSystems/)**<br><sub>University of Illinois, 2024</sub> | book, code |  |  |  |
| **[Robotic Manipulation: Perception, Planning, and Control](https://manipulation.mit.edu)**<br><sub>MIT (online)</sub> | book, code |  | Drake |  |
| **[Underactuated Robotics: Algorithms for Walking, Running, Swimming, Flying, and Manipulation](https://underactuated.mit.edu/)**<br><sub>MIT (online), 2024</sub> | book, code |  | Drake |  |
| **[Robotics: Modelling, Planning and Control](https://link.springer.com/book/10.1007/978-1-84628-642-1)**<br><sub>Springer, 2009</sub> | — |  |  |  |
| **[Foundations of Robotics (course notes)](https://rpal.cs.cornell.edu/foundations)**<br><sub>Cornell University</sub> | book |  |  |  |

<details><summary>Details: offerings, sources of each material, notes</summary>

**Introduction to Autonomous Mobile Robots (2nd ed.)** — R. Siegwart, I. R. Nourbakhsh, D. Scaramuzza (MIT Press)

- Offering: [MIT Press (2nd ed., 2011)](https://bookshop.org/p/books/introduction-to-autonomous-mobile-robots-second-edition-davide-scaramuzza/a2f4851c1824469c) — paid
- Materials: Book: paid
- Used by: Autonomous Mobile Robots
- The textbook of ETH AMR.

**Introduction to Autonomous Robots** — N. Correll, B. Hayes, C. Heckman, A. Roncone (MIT Press / open source)

- Offering: [Book site](https://introduction-to-autonomous-robots.github.io) — free
- Offering: [Source and releases on GitHub](https://github.com/Introduction-to-Autonomous-Robots/Introduction-to-Autonomous-Robots/releases) — free
- Offering: [Open Textbook Library](https://open.umn.edu/opentextbooks/textbooks/316) — free
- Materials: Book: free (LaTeX source (CC BY-NC-ND); older compiled editions on GitHub; print by MIT Press)
- Used by: Introduction to Robotics (CSCI 3302)
- Mechanisms, sensors, actuators and algorithms; the textbook of CU CSCI 3302.

**Robotics, Vision and Control: Fundamental Algorithms in Python (3rd ed.)** — P. Corke (Springer)

- Offering: [Book site](https://petercorke.com/rvc3p/home/) — free
- Offering: [Springer](https://link.springer.com/book/10.1007/978-3-031-06469-2) — paid
- Offering: [Code and notebooks for every chapter](https://github.com/petercorke/RVC3-python) — free
- Materials: Book: paid; Code: free (RVC3-python (Jupyter notebooks for all chapters))
- Used by: Robot Academy
- Broad and very practical; every figure can be reproduced with the Python toolboxes. A MATLAB edition also exists.

**Introduction to Robotics and Perception** — F. Dellaert, S. Hutchinson (Georgia Tech (online, draft))

- Offering: [Online interactive book](https://www.roboticsbook.org/intro.html) — free
- Offering: [Notebooks on GitHub](https://github.com/gtbook/robotics) — free
- Materials: Book: free (online (read only; code BSD-3)); Code: free
- Used by: Introduction to Robotics and Perception (CS 3630)
- Every section is a runnable notebook; probabilistic and factor-graph view of robotics.

**Elements of Robotics** — M. Ben-Ari, F. Mondada (Springer (open access))

- Offering: [Springer (open access, CC BY)](https://link.springer.com/book/10.1007/978-3-319-62533-1) — free
- Materials: Book: free
- Used by: Introduction to Robotics (Hanze)
- Gentle, algorithm-first introduction with educational Thymio robot examples; used by the Hanze course.

**Modern Robotics: Mechanics, Planning, and Control** — K. M. Lynch, F. C. Park (Cambridge University Press)

- Offering: [Free preprint and videos](https://hades.mech.northwestern.edu/index.php/Modern_Robotics) — free
- Materials: Book: free (preprint PDF); Video: free; Code: free
- Used by: Modern Robotics
- The book of the Modern Robotics MOOC.

**Probabilistic Robotics** — S. Thrun, W. Burgard, D. Fox (MIT Press)

- Offering: [Book page](https://robots.stanford.edu/probabilistic-robotics/) — paid
- Materials: Book: paid
- Used by: Lectures of Cyrill Stachniss (Robot Mapping, Mobile Sensing and Robotics, Self-Driving Cars)
- The reference for Bayes, Kalman and particle filters, Markov localization and SLAM; its notation is used by Stanford PoRA.

**State Estimation for Robotics (2nd ed.)** — T. D. Barfoot (Cambridge University Press)

- Offering: [Author's page (unofficial PDF)](https://asrl.utias.utoronto.ca/~tdb/) — free
- Materials: Book: free (author's unofficial PDF)
- Rigorous treatment of Gaussian estimation, matrix Lie groups and batch/continuous-time estimation.

**Planning Algorithms** — S. M. LaValle (Cambridge University Press)

- Offering: [Full book online](https://lavalle.pl/planning/) — free
- Materials: Book: free (HTML and PDF chapters)
- The standard reference on discrete, sampling-based and combinatorial motion planning.

**Robotic Systems (draft)** — K. Hauser (University of Illinois)

- Offering: [Online book with notebooks](https://motion.cs.illinois.edu/RoboticSystems/) — free
- Materials: Book: free (HTML and Jupyter (some chapters incomplete)); Code: free (Klampt (Python))
- Systems-level view of robotics with runnable notebooks.

**Robotic Manipulation: Perception, Planning, and Control** — R. Tedrake (MIT (online))

- Offering: [Online textbook](https://manipulation.mit.edu) — free
- Materials: Book: free; Code: free (Drake notebooks)
- Used by: Robotic Manipulation (6.4210 / 6.4212)

**Underactuated Robotics: Algorithms for Walking, Running, Swimming, Flying, and Manipulation** — R. Tedrake (MIT (online))

- Offering: [Online notes](https://underactuated.mit.edu/) — free
- Materials: Book: free; Code: free (Drake notebooks)
- Used by: Underactuated Robotics (6.832)

**Robotics: Modelling, Planning and Control** — B. Siciliano, L. Sciavicco, L. Villani, G. Oriolo (Springer)

- Offering: [Springer](https://link.springer.com/book/10.1007/978-1-84628-642-1) — paid
- Materials: Book: paid
- Used by: Introduction to Robotics (CS 223A)
- Supplementary text of Stanford CS 223A.

**Foundations of Robotics (course notes)** — R. A. Knepper, C. Mavrogiannis, J. Proft, W. Thomason (Cornell University)

- Offering: [Course notes (PDF chapters)](https://rpal.cs.cornell.edu/foundations) — free
- Materials: Book: free (PDF chapters (copyrighted, readable online))
- Notes of Cornell CS 4750: mechanisms, simulation, kinematics, uncertainty, optimization and control.

</details>

## Video lecture series

Video collections that are not tied to a single course above.

| Resource | Free online | Textbook | Software | Other ways to take it |
|---|---|---|---|---|
| **[Robot Academy](https://petercorke.com/resources/robot-academy/)**<br><sub>Queensland University of Technology, 2017</sub> | video | [Robotics, Vision and Control](https://petercorke.com/rvc3p/home/) |  |  |
| **[Lectures of Cyrill Stachniss (Robot Mapping, Mobile Sensing and Robotics, Self-Driving Cars)](https://www.ipb.uni-bonn.de/teaching)**<br><sub>University of Bonn, 2021</sub> | video<br><sub>partly: slides, exercises</sub> | [Probabilistic Robotics](https://robots.stanford.edu/probabilistic-robotics/) |  | [Robot Mapping (slides and videos)](https://www.ipb.uni-bonn.de/robot-mapping/)<br>[Robot Mapping YouTube playlist](https://www.youtube.com/playlist?list=PLgnQpQtFTOGQrZ4O5QzbIHgl3b1JHimN_)<br>[Mobile Sensing and Robotics II (2021)](https://www.ipb.uni-bonn.de/msr2-2021/index.html)<br>[Techniques for Self-Driving Cars](https://www.ipb.uni-bonn.de/sdc-2021/index.html) |

<details><summary>Details: offerings, sources of each material, notes</summary>

**Robot Academy** — P. Corke (Queensland University of Technology)

- Offering: [Robot Academy](https://petercorke.com/resources/robot-academy/) — free
- Materials: Video: free (over 200 short lessons and masterclasses)
- Textbook: Robotics, Vision and Control: Fundamental Algorithms in Python (3rd ed.)
- Short, well-produced video lessons that follow the Robotics, Vision and Control book.

**Lectures of Cyrill Stachniss (Robot Mapping, Mobile Sensing and Robotics, Self-Driving Cars)** — C. Stachniss (University of Bonn)

- Offering: [Teaching page with links](https://www.ipb.uni-bonn.de/teaching) — free
- Offering: [Robot Mapping (slides and videos)](https://www.ipb.uni-bonn.de/robot-mapping/) — free
- Offering: [Robot Mapping YouTube playlist](https://www.youtube.com/playlist?list=PLgnQpQtFTOGQrZ4O5QzbIHgl3b1JHimN_) — free
- Offering: [Mobile Sensing and Robotics II (2021)](https://www.ipb.uni-bonn.de/msr2-2021/index.html) — free
- Offering: [Techniques for Self-Driving Cars](https://www.ipb.uni-bonn.de/sdc-2021/index.html) — free
- Materials: Slides: partial (Robot Mapping course page); Video: free (YouTube playlists); Exercises: partial (2020 exercise archive)
- Textbook: Probabilistic Robotics
- Probably the clearest video explanations of Kalman and particle filters, EKF and graph SLAM.

</details>

## Labs, exercises and notebooks

Ready-to-use exercises, labs and Jupyter notebooks.

| Resource | Free online | Textbook | Software | Other ways to take it |
|---|---|---|---|---|
| **[Robotics Simulation Labs and Mobile Robot Control notebooks](https://github.com/felipenmartins/Robotics-Simulation-Labs)**<br><sub>Hanze University of Applied Sciences</sub> | exercises, code |  | Webots | [Mobile Robot Control notebooks](https://github.com/felipenmartins/Mobile-Robot-Control) |
| **[Jupyter notebooks for robotics courses](https://github.com/jotaraul/jupyter-notebooks-for-robotics-courses)**<br><sub>University of Málaga (MAPIR)</sub> | exercises, code |  | Python |  |
| **[Introduction to Robotics with Drones (Duckiedrone)](https://docs.duckietown.com/ente/course-intro-to-drones/intro.html)**<br><sub>Duckietown</sub> | notes, exercises |  |  |  |

<details><summary>Details: offerings, sources of each material, notes</summary>

**Robotics Simulation Labs and Mobile Robot Control notebooks** — F. N. Martins (Hanze University of Applied Sciences)

- Offering: [Robotics Simulation Labs](https://github.com/felipenmartins/Robotics-Simulation-Labs) — free
- Offering: [Mobile Robot Control notebooks](https://github.com/felipenmartins/Mobile-Robot-Control) — free
- Materials: Exercises: free; Code: free
- Built for: Introduction to Robotics (CSCI 3302)
- Nine Webots labs from installation to Dijkstra, plus Jupyter notebooks on mobile-robot control.

**Jupyter notebooks for robotics courses** — S. F. Baltanás, J. R. Ruiz-Sarmiento, J. González-Jiménez (University of Málaga (MAPIR))

- Offering: [GitHub](https://github.com/jotaraul/jupyter-notebooks-for-robotics-courses) — free
- Materials: Exercises: free; Code: free
- Notebook exercises on motion, sensing, localization (EKF, particle filter), mapping, SLAM and planning.

**Introduction to Robotics with Drones (Duckiedrone)** —  (Duckietown)

- Offering: [Online textbook and projects](https://docs.duckietown.com/ente/course-intro-to-drones/intro.html) — free
- Materials: Notes: free; Exercises: free (projects: PID altitude control, UKF, localization, SLAM)
- Build-your-own drone course; hardware kit required for the full experience.

</details>

## Robot learning, physical AI and embodied AI

Courses and tutorials on learning-based robotics, and introductions to physical and embodied AI.

| Resource | Free online | Textbook | Software | Other ways to take it |
|---|---|---|---|---|
| **[Principles of Robot Autonomy II (CS 237B)](https://web.stanford.edu/class/cs237b/)**<br><sub>Stanford University, 2025</sub> | slides, notes<br><sub>partly: exercises, code</sub> |  | ROS 2 |  |
| **[Hugging Face Robotics Course](https://huggingface.co/learn/robotics-course)**<br><sub>Hugging Face, 2025</sub> | code<br><sub>partly: notes</sub> |  | LeRobot |  |
| **[Robot Learning: A Tutorial](https://huggingface.co/spaces/lerobot/robot-learning-tutorial)**<br><sub>Hugging Face, 2025</sub> | notes, code |  | LeRobot | [arXiv 2510.12403](https://arxiv.org/abs/2510.12403) |
| **[Robot Learning (CS 4756 / 5756)](https://www.cs.cornell.edu/courses/cs4756/2026sp/)**<br><sub>Cornell University, 2026</sub> | slides, exercises, code |  | Python |  |
| **[Embodied AI (CS 539)](https://web.engr.oregonstate.edu/~leestef/courses/2019/fall/cs539.html)**<br><sub>Oregon State University, 2019</sub> | slides |  |  |  |
| **[What is physical AI? Introductory articles](https://towardsdatascience.com/physical-ai-what-it-is-and-what-it-is-not/)**<br><sub>2025</sub> | notes |  |  | [A beginner's guide to physical AI](https://tacticzhazel.substack.com/p/a-beginners-guide-to-physical-ai)<br>[HumynLabs: What is physical AI (robotics, embodied AI)](https://humynlabs.ai/blog/what-is-physical-ai-robotics-embodied-ai-explained)<br>[Universal Robots webinar: physical AI](https://video.universal-robots.com/discover-how-physical-ai-is-1) |

<details><summary>Details: offerings, sources of each material, notes</summary>

**Principles of Robot Autonomy II (CS 237B)** — J. Bohg, M. Pavone, D. Sadigh (Stanford University)

- Offering: [Course site, winter 2025](https://web.stanford.edu/class/cs237b/) — free
- Materials: Book: not available; Slides: free (course site (16 lectures)); Notes: free (course site); Video: not available (Canvas only); Exercises: partial (homework page); Solutions: not available; Code: partial (Colab notebooks)
- Reinforcement learning, imitation learning, learning-based perception and manipulation, human-robot interaction.

**Hugging Face Robotics Course** —  (Hugging Face)

- Offering: [Course](https://huggingface.co/learn/robotics-course) — free
- Materials: Notes: partial (units 0–2 published; RL, imitation and foundation-model units announced); Code: free (LeRobot)

**Robot Learning: A Tutorial** — F. Capuano, C. Pascal, A. Zouitine, T. Wolf, M. Aractingi (Hugging Face)

- Offering: [Interactive tutorial (Hugging Face Space)](https://huggingface.co/spaces/lerobot/robot-learning-tutorial) — free
- Offering: [arXiv 2510.12403](https://arxiv.org/abs/2510.12403) — free
- Materials: Notes: free; Code: free (LeRobot examples)
- From RL and behavioural cloning to generalist vision-language-action models, with runnable LeRobot code.

**Robot Learning (CS 4756 / 5756)** — K. Fang (Cornell University)

- Offering: [Course site, spring 2026](https://www.cs.cornell.edu/courses/cs4756/2026sp/) — free
- Materials: Slides: free (slides for every lecture); Exercises: free (six assignments on GitHub); Code: free
- Imitation learning, deep RL, model-based control, visuomotor policies and foundation models.

**Embodied AI (CS 539)** — S. Lee (Oregon State University)

- Offering: [Course page, fall 2019](https://web.engr.oregonstate.edu/~leestef/courses/2019/fall/cs539.html) — free
- Materials: Slides: free (lecture slides (pptx))
- Paper-reading seminar on visual navigation, instruction following, embodied question answering and sim2real.

**What is physical AI? Introductory articles** — 

- Offering: [Towards Data Science: Physical AI, what it is and what it is not](https://towardsdatascience.com/physical-ai-what-it-is-and-what-it-is-not/) — free
- Offering: [A beginner's guide to physical AI](https://tacticzhazel.substack.com/p/a-beginners-guide-to-physical-ai) — free
- Offering: [HumynLabs: What is physical AI (robotics, embodied AI)](https://humynlabs.ai/blog/what-is-physical-ai-robotics-embodied-ai-explained) — free
- Offering: [Universal Robots webinar: physical AI](https://video.universal-robots.com/discover-how-physical-ai-is-1) — free
- Materials: Notes: free
- Popular-science introductions with good graphics; useful for a motivating first lecture.

</details>

## Simulators and software for teaching

Simulators, libraries and tools used by the courses above.

| Software | Developer | License | Used by | Notes |
|---|---|---|---|---|
| [Webots](https://cyberbotics.com) | Cyberbotics | Apache 2.0 | Introduction to Robotics (CSCI 3302), Introduction to Robotics (Hanze), Robotics Simulation Labs and Mobile Robot Control notebooks | Open-source desktop robot simulator with many ready robot models (e-puck, TurtleBot, Pioneer); Python, C, C++, MATLAB. |
| [CoppeliaSim (formerly V-REP)](https://www.coppeliarobotics.com) | Coppelia Robotics | Free educational license | Autonomous Mobile Robots, Modern Robotics | Versatile simulator with remote APIs for Python and MATLAB. |
| [MuJoCo](https://mujoco.org) | Google DeepMind | Apache 2.0 |  | Fast physics engine for contact-rich simulation and robot learning; Python bindings. |
| [Gazebo](https://gazebosim.org) | Open Robotics | Apache 2.0 |  | The standard simulator of the ROS ecosystem. |
| [NVIDIA Isaac Sim and Isaac Lab](https://developer.nvidia.com/isaac/sim) | NVIDIA | Apache 2.0 (plus NVIDIA additional materials license) |  | Photorealistic GPU simulator for perception and large-scale robot learning; needs an NVIDIA RTX GPU. |
| [CARLA](https://carla.org) | CARLA team (CVC, Intel Labs) | MIT | Self-Driving Cars Specialization | Open-source simulator for autonomous driving. |
| [ROS 2](https://docs.ros.org) | Open Robotics | Apache 2.0 | Principles of Robot Autonomy I (AA 174A / AA 274A), Principles of Robot Autonomy II (CS 237B), Artificial Intelligence for Robotics | The robot middleware used in industry and in many courses. |
| [ROS (1)](https://wiki.ros.org) | Open Robotics | BSD | Self-Driving Cars with Duckietown | The original Robot Operating System; end of life in 2025, replaced by ROS 2. |
| [Drake](https://drake.mit.edu) | Toyota Research Institute / MIT | BSD-3 | Robotic Manipulation (6.4210 / 6.4212), Underactuated Robotics (6.832), Robotic Manipulation: Perception, Planning, and Control, Underactuated Robotics: Algorithms for Walking, Running, Swimming, Flying, and Manipulation | Model-based design and optimisation toolbox used by the MIT manipulation and underactuated courses. |
| [Python Robotics Ecosystem (Robotics Toolbox, Spatial Maths, Machine Vision Toolbox, Swift)](https://github.com/petercorke/robotics-toolbox-python) | QUT | MIT | Robotics, Vision and Control: Fundamental Algorithms in Python (3rd ed.) | The Python toolboxes behind Robotics, Vision and Control, with the browser-based Swift simulator. |
| [PythonRobotics](https://atsushisakai.github.io/PythonRobotics/) | A. Sakai et al. | MIT |  | Short, readable Python implementations of classic algorithms (EKF, particle filter, A*, RRT, pure pursuit) with animations. |
| [GTSAM](https://gtsam.org) | Georgia Tech | BSD | Introduction to Robotics and Perception (CS 3630), Introduction to Robotics and Perception | Factor-graph library for estimation and SLAM, with Python bindings; used by the Dellaert & Hutchinson book. |
| [OMPL (Open Motion Planning Library)](https://ompl.kavrakilab.org) | Rice University (Kavraki Lab) | BSD |  | Sampling-based planners (PRM, RRT and many variants) with Python bindings. |
| [LeRobot](https://github.com/huggingface/lerobot) | Hugging Face | Apache 2.0 | Hugging Face Robotics Course, Robot Learning: A Tutorial | PyTorch library, datasets and pretrained policies for real-world robot learning (low-cost SO-100/101 arms). |
| [Crazyflie (Bitcraze)](https://www.bitcraze.io) | Bitcraze | Open source (GPL-3.0 firmware) | Introduction to Robotics (MAE 345 / ECE 345 / COS 346) | Open-source palm-sized quadrotor platform used by Princeton MAE 345. |
| [Drift](https://docs.godrift.ai/getting-started/introduction) | Drift (startup) | Proprietary (free tier) |  | AI copilot on the command line for setting up and debugging ROS / Gazebo simulations. |

## Which course uses which book and software

| Course | Siegwart et al. | Correll et al. | Robotics, Vision and Control | Dellaert & Hutchinson | Elements of Robotics | Modern Robotics (book) | Probabilistic Robotics | Robotic Manipulation (book) | Underactuated Robotics (book) | Siciliano et al. | Webots | CoppeliaSim | CARLA | ROS 2 | ROS 1 | Drake | Robotics Toolbox (Python) | GTSAM | LeRobot | Crazyflie | Python | MATLAB |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| ETH AMR | ● |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  | ● |
| Stanford PoRA I |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  | ● |  |
| Stanford PoRA II |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  | ● |  |
| Stanford CS 223A |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| GA Tech CS 3630 |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  | ● |  |
| CU CSCI 3302 |  | ● |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  | ● |  |
| Hanze Intro to Robotics |  |  |  |  | ● |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  | ● |  |
| Princeton MAE 345 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● | ● |  |
| MIT Manipulation |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  | ● |  |  |  |  | ● |  |
| MIT Underactuated |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  | ● |  |  |  |  | ● |  |
| CMU 16-362 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |
| Duckietown MOOC |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  | ● |  |
| Modern Robotics (MOOC) |  |  |  |  |  | ● |  |  |  |  |  | ● |  |  |  |  |  |  |  |  | ● | ● |
| Toronto Self-Driving Cars |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  | ● |  |
| Penn Robotics |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| Packt AI for Robotics |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  | ● |  |
| Robot Academy |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Stachniss lectures (Bonn) |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Martins labs |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  | ● |  |
| Málaga notebooks |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |
| Hugging Face course |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |
| Robot Learning tutorial |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |
| Cornell CS 4756 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |

## How to contribute

All data is in [`resources.yaml`](resources.yaml). Edit or add an entry, run `python build.py`, and open a pull request. The README and the web page are generated from the YAML file; do not edit them by hand. The format of an entry is described at the top of the YAML file.

Last checked: November 2026.
