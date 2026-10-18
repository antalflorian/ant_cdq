# Smart Braking Assistant (ROS 2)

Ez a csomag egy önvezető járművekhez készült intelligens fékasszisztenst (Smart Braking Assistant) valósít meg ROS 2 környezetben (Humble).
A projekt az "Autonóm járművek és robotok programozása" tárgy kis beadandó feladataként készült.

## Funkciók
* **smart_braking_assistant:** A fő node, amely a `/front_distance` topic-on figyeli az akadályok távolságát, és sebességparancsokat (`/speed_command`) ad ki (tiszta út, lassítás, vészfékezés).
* **obstacle_simulator:** Tesztelő node, amely folyamatosan közeledő akadályt szimulál a teszteléshez.
* **Paraméterezhetőség:** A biztonságos távolság és a sebesség ROS 2 paraméterekként dinamikusan állítható a `launch` fájlban.

## Build
A package a következő parancssal buildelhető:
```bash
colcon build --packages-select smart_braking_assistant

## Futtatás
A teljes rendszer (a szimulátorral és a vezérlővel együtt) egyetlen paranccsal elindítható:

```bash
ros2 launch smart_braking_assistant smart_braking.launch.py