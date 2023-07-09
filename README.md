![Fuzzy Sets](https://raw.githubusercontent.com/Education-IT/Fuzzy-Sets/main/images/banner.png)
## Final project for the course - ***Artificial Intelligence*** - **UAM**

> **Completed during the fourth semester of computer science studies.**

The task was to use **fuzzy sets** to create a program that recommends movies to the user based on specified, fuzzy, **vague filters**. I created **6 functions** that assign a value from **0** to **1** to movies based on their compatibility with the designated filter. The program generates 3 newly created `.csv` files that contain the recommended movies that best match the user's selection. The files are sorted based on the values assigned by the **membership function**.

![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white) ![Microsoft Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white) [![website](https://img.shields.io/badge/website-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://education-it.pl/)
 ## 
**Program:**
1) It starts with a movie database - `database.csv`.
2) Using the implemented 6 **mathematical functions**, it creates lists with the membership function values ranging from **0** to **1**.
3) It calculates the **minimum t-norm** and **maximum k-norm** of 2 specific designated filters.
4) It sorts the movies from most to least suitable, considering only **positive values** assigned by the membership function.
4) It creates 3 `.csv` files:
   a) `recommended_movies_fairly_new_and_medium_length.csv`
   b) `medium_aged_or_not_long.csv`
   c) `old_and_fairly_long.csv`

## Functions:
- The presented diagrams are illustrative. They represent the behavior of the functions only for a specific set of movies (`database.csv`).
- The functions that determine the filter's fit from the perspective of the movie's release date were designed to be universal and reusable in the future. These membership functions take into account the current year.

##

### 1. Fairly New Movies:

> $$f(x)  =
 \begin{cases}
 x = [ movieYear - (currentYear - 8) ]/3 & \quad  \text{if } x > (currentYear - 8) \text{ and } x < (currentYear - 5)\\
  x=[ (currentYear -1) - movieYear]/3 & \quad  \text{if } x > (currentYear - 4) \text{ and }  x < (currentYear - 1)\\
  1 & \quad  \text{if } x \ge (currentYear - 5) \text{ and } x \le (currentYear-4) \\
  0 & \quad  \text{if }  x \ge (currentYear - 1) \text{ or } x < (currentYear - 8)\\
  \end{cases}$$

![enter image description here](https://github.com/Education-IT/Fuzzy-Sets/blob/main/diagrams/filmy_w_miare_nowe.JPG?raw=true)
##

 ### 2. Medium Aged Movies:

> $$f(x)  =
  \begin{cases}
 x = [ movieYear - (currentYear -30) ]/6 & \quad  \text{if } x > (currentYear -30) \text{ and  } x < (currentYear -20) \\
  x=[ (currentYear - 14) - movieYear]/6 & \quad  \text{if } x > (currentYear -20) \text{ and }  x < (currentYear - 14)\\
  1 & \quad  \text{if } x \ge (currentYear-24) \text{ and } x \le (currentYear-20) \\
  0 & \quad  \text{if } x > (currentYear - 14) \text{ or } x < (currentYear - 30) \\
  \end{cases}$$
  
  ![enter image description here](https://github.com/Education-IT/Fuzzy-Sets/blob/main/diagrams/srednio_stary_film.JPG?raw=true)
##

 ### 3. Old Movies:

> $$f(x)  =
  \begin{cases}
 x = [ movieYear - (currentYear - 42) ]/12 & \quad  \text{if } x < (currentYear - 30) \text{ and } x > (currentYear-44)\\
  1 & \quad  \text{if } x \le (currentYear -44)\\
 0 & \quad  \text{if }  x > (currentYear - 30) \\
  \end{cases}$$

![enter image description here](https://github.com/Education-IT/Fuzzy-Sets/blob/main/diagrams/filmy_stare.JPG?raw=true)

##

### 4. Not Long Movies:

> $$f(x)  =
  \begin{cases}
 x = [ movieLength - 60  ]/18 & \quad  \text{if } x\in(60, 78]\\
  x=[100- movieLength]/18 & \quad  \text{if } x\in (82,100]\\
  1 & \quad  \text{if } x \in [78,82]\\
  0 & \quad  \text{for other x values}\\
  \end{cases}$$

![enter image description here](https://github.com/Education-IT/Fuzzy-Sets/blob/main/diagrams/filmy_niedugie.JPG?raw=true)
##

### 5. Medium Length Movies:

> $$f(x)  =
  \begin{cases}
 x = [ movieLength - 99  ]/9 & \quad  \text{if } x\in (99 , 108]\\
  x=[119- movieLength]/9 & \quad  \text{if } x\in (110,119]\\
  1 & \quad  \text{if } x \in [108,110]\\
  0 & \quad  \text{for other x values}\\
  \end{cases}$$

![enter image description here](https://github.com/Education-IT/Fuzzy-Sets/blob/main/diagrams/filmy_srednio_dlugie.JPG?raw=true)
##

### 6. Fairly Long Movies:

> $$f(x)  =
  \begin{cases}
 x = [ movieLength - 110]/16 & \quad  \text{if } x\in (110, 126]\\
  x=[142- movieLength]/16 & \quad  \text{if } x\in (126,142]\\
  1 & \quad  \text{if } x = 126\\
  0 & \quad  \text{for other x values}\\
  \end{cases}$$

![enter image description here](https://github.com/Education-IT/Fuzzy-Sets/blob/main/diagrams/filmy_dosc_dlugie.JPG?raw=true)
##


## What have I Learned
- This project was a perfect exercise for applying the newly acquired knowledge of fuzzy logic.
- I solidified the process of comparing multiple values from different membership functions (**minimum t-norm** and **maximum k-norm**).
- It made me realize how easily but thoughtfully fuzzy logic can be practically applied to implement various useful programs. For example, in e-commerce stores, where we often define a precise price range of interest, but a slightly more expensive product with specific features may be more appealing. Unfortunately, such stores, when presenting search results, do not take into account products that slightly deviate from certain parameters but are clearly a better fit in other aspects.
