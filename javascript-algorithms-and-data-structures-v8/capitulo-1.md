# Learn Basic JavaScript by building a role Playing game
### Paso 1:
[Enlace](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/learn-basic-javascript-by-building-a-role-playing-game/step-1)
```html
<!doctype html>
<html  lang="en">
<head>
<meta  charset="UTF-8"  />
<link  rel="icon"  type="image/svg+xml"  href="/vite.svg"  />
<meta  name="viewport"  content="width=device-width, initial-scale=1.0"  />
<link  rel="stylesheet"  href="styles.css">
<title>RPG - Dragon Repeller</title>
</head>
<body>
<div  id="game"></div>
</body>
</html>
```

### Paso 2
[Enlace](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/learn-basic-javascript-by-building-a-role-playing-game/step-2)
```html
<script></script>
```

### Paso 3
[Enlace](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/learn-basic-javascript-by-building-a-role-playing-game/step-3)
```html
<script>
console.log("Hello World");
</script>
```

### Paso 4
[Enlace](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/learn-basic-javascript-by-building-a-role-playing-game/step-4)
```html
<script  src="./script.js"></script>
```

### Paso 5
[Enlace](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/learn-basic-javascript-by-building-a-role-playing-game/step-5)

```JavaScript
console.log("Hello World");
```

### Paso 6
[Enlace](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/learn-basic-javascript-by-building-a-role-playing-game/step-6)

```JS
let  xp;
```

### Paso 7
[Enlace](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/learn-basic-javascript-by-building-a-role-playing-game/step-7)

```JS
let  xp = 0;
```


### Paso 8
[Enlace](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/learn-basic-javascript-by-building-a-role-playing-game/step-8)

```JS
let  xp = 0;
let  health = 100
let  gold = 50
```
### Paso 9
[Enlace](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/learn-basic-javascript-by-building-a-role-playing-game/step-9)

```JS
let  xp = 0;
let  health = 100;
let  gold = 50;
let  currentWeapon = 0
```

### Paso 10
[Enlace](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/learn-basic-javascript-by-building-a-role-playing-game/step-10)

```JS
let  xp = 0;
let  health = 100;
let  gold = 50;
let  currentWeapon = 0;
let  fighting;
```

### Paso 11
[Enlace](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/learn-basic-javascript-by-building-a-role-playing-game/step-11)

```JS
let  xp = 0;
let  health = 100;
let  gold = 50;
let  currentWeapon = 0;
let  fighting;
let  monsterHealth;
let  inventory;
```

### Paso 12
[Enlace](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/learn-basic-javascript-by-building-a-role-playing-game/step-12)

```JS
let  xp = 0;
let  health = 100;
let  gold = 50;
let  currentWeapon = 0;
let  fighting;
let  monsterHealth;
let  inventory = 'stick';
```

### Paso 13
[Enlace](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/learn-basic-javascript-by-building-a-role-playing-game/step-13)

```JS
let  xp = 0;
let  health = 100;
let  gold = 50;
let  currentWeapon = 0;
let  fighting;
let  monsterHealth;
let  inventory = ["stick", "dagger", "sword"];
```

### Paso 14
[Enlace](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/learn-basic-javascript-by-building-a-role-playing-game/step-14)

```JS
let  xp = 0;
let  health = 100;
let  gold = 50;
let  currentWeapon = 0;
let  fighting;
let  monsterHealth;
let  inventory = ["stick"];
```
### Paso 15
[Enlace](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/learn-basic-javascript-by-building-a-role-playing-game/step-15)

```html
<body>
<div  id="game">
<div  id="stats"></div>
<div  id="controls"></div>
<div  id="monsterStats"></div>
<div  id="text"></div>
</div>
</body>
```
### Paso 16
[Enlace](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/learn-basic-javascript-by-building-a-role-playing-game/step-16)

```html
<body>
<div  id="game">
<div  id="stats">
	<span  class="stat">XP: 0</span>
	<span  class="stat">Health: 100</span>
	<span  class="stat">Gold: 50</span>
</div>
<div  id="controls"></div>
<div  id="monsterStats"></div>
<div  id="text"></div>
</div>
</body>
```
### Paso 17
[Enlace](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/learn-basic-javascript-by-building-a-role-playing-game/step-17)

```html
<span class="stat">XP: <strong>
    <span id="xpText">0</span>
  </strong>
</span>
<span class="stat">Health: <strong>
    <span id="healthText">100</span>
  </strong>
</span>
<span class="stat">Gold: <strong>
    <span id="goldText">50</span>
  </strong>
</span>
```

### Paso 18
[Enlace](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/learn-basic-javascript-by-building-a-role-playing-game/step-18)

```html
<div  id="controls">
	<button  id="button1">Go to store</button>
	<button  id="button2">Go to cave</button>
	<button  id="button3">Fight dragon</button>
</div>
```

### Paso 19
[Enlace](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/learn-basic-javascript-by-building-a-role-playing-game/step-19)

```JS
let  button1 = document.querySelector("#button1")
```

### Paso 20
[Enlace](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/learn-basic-javascript-by-building-a-role-playing-game/step-20)

```html
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="./styles.css">
  <title>RPG - Dragon Repeller</title>
</head>
<body>
  <div id="game">
    <div id="stats">
      <span class="stat">XP: <strong>
          <span id="xpText">0</span>
        </strong>
      </span>
      <span class="stat">Health: <strong>
          <span id="healthText">100</span>
        </strong>
      </span>
      <span class="stat">Gold: <strong>
          <span id="goldText">50</span>
        </strong>
      </span>
    </div>
    <div id="controls">
      <button id="button1">Go to store</button>
      <button id="button2">Go to cave</button>
      <button id="button3">Fight dragon</button>
    </div>
    <div id="monsterStats"></div>
    <div id="text"></div>
  </div>
  <script src="./script.js"></script>
</body>
```