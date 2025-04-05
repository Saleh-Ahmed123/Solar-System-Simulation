import math
import matplotlib.pyplot as plt

G = 6.67*10**-11

class CelestialBody:
    def __init__(self, name, mass, x, y, vx, vy):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.name = name
        all_bodies.add_body(self)


class AllBodies:
    def __init__(self):
        self.bodies = []
        self.time_step = 86400
        self.time = 3.154*10**7

    def add_body(self, body):
        self.bodies.append(body)

    def orbits(self):
        maxX = 0
        minX = 0
        maxY = 0
        minY = 0

        for body in self.bodies:
            if body != Sun:
                x_values = []
                y_values = []
                for count in range(60190):


                    ForceX = 0
                    ForceY = 0

                    for other_body in self.bodies:
                        if other_body != body:
                            r = math.sqrt((body.x - other_body.x) ** 2 + (body.y - other_body.y) ** 2)
                            Force = -(G * other_body.mass * body.mass) / r ** 2

                            ForceX += Force * body.x / r
                            ForceY += Force * body.y / r


                    AccelerationX = ForceX/body.mass
                    AccelerationY = ForceY/body.mass

                    New_vx = AccelerationX * self.time_step
                    New_vy = AccelerationY * self.time_step

                    body.vx += New_vx
                    body.vy += New_vy

                    body.x += body.vx * self.time_step
                    body.y += body.vy * self.time_step

                    x_values.append(body.x)
                    y_values.append(body.y)


                if max(x_values) > maxX:
                    maxX = max(x_values)

                if max(y_values) > maxY:
                    maxY = max(y_values)

                if min(x_values) < minX:
                    minX = min(x_values)

                if min(y_values) < minY:
                    minY = min(y_values)
                plt.plot(x_values, y_values, label = body.name)

        sun_circle = plt.Circle((0, 0), 6.9634*10**9, color='yellow', label="Sun")
        plt.gca().add_artist(sun_circle)
        plt.xlim(minX, maxX)
        plt.ylim(minY, maxY)
        plt.legend()
        plt.show()



all_bodies = AllBodies()
Sun = CelestialBody("Sun", 1.989*10**30, 0,0,0,0)
Mercury = CelestialBody("Mercury", 3.285 * 10**23, 0, 67999000000, 47000, 0)
Venus = CelestialBody("Venus", 4.867 * 10**24, 0, 108200000000, 35000, 0)
Earth = CelestialBody("Earth", 5.972 * 10**24, 0, 149597870700, 30000, 0)
Mars = CelestialBody("Mars", 6.419 * 10**23, 0, 227943824000, 24000, 0)
Jupiter = CelestialBody("Jupiter", 1.898 * 10**27, 0, 778579000000, 13000, 0)
Saturn = CelestialBody("Saturn", 5.683 * 10**26, 0, 1426790000000, 9700, 0)
Uranus = CelestialBody("Uranus", 8.681 * 10**25, 0, 2870970000000, 6800, 0)
Neptune = CelestialBody("Neptune", 1.024 * 10**26, 0, 4498390000000, 5400, 0)


all_bodies.orbits()