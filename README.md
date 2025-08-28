#week 5 readme file.
# Assignment qtn 1.

## Overview

This Python program implements an Object-Oriented Programming (OOP) assignment featuring a `Superhero` base class and a `FlyingSuperhero` subclass. It demonstrates **encapsulation**, **inheritance**, and **polymorphism** through a simple superhero-themed system.

## Purpose

The program models superheroes with attributes (name, power, missions) and methods (display info, complete missions, use powers). The `FlyingSuperhero` subclass extends this with flying-specific features, showcasing OOP principles.

## Class Structure

1. **Superhero Class**:

   - **Attributes** (protected with `_` for encapsulation):
     - `_name`: Superhero's name (e.g., "Thunder").
     - `_power`: Superhero's power (e.g., "Strength").
     - `_missions`: Number of missions completed (starts at 0).
   - **Methods**:
     - `get_name()`: Returns the superhero's name.
     - `show_info()`: Displays name, power, and missions.
     - `do_mission()`: Increments missions and confirms completion.
     - `use_power()`: Describes using the superhero's power.

2. **FlyingSuperhero Class** (inherits from `Superhero`):

   - **Additional Attribute**:
     - `_speed`: Flying speed in mph (e.g., 200).
   - **Methods**:
     - `use_power()`: Overrides to describe flying with power and speed (polymorphism).
     - `fly(place)`: Describes flying to a location

## OOP Concepts

- **Encapsulation**: Attributes are protected (using `_`) and accessed via methods.
- **Inheritance**: `FlyingSuperhero` inherits from `Superhero`, reusing its attributes and methods.
- **Polymorphism**: `use_power()` behaves differently in `Superhero` (generic) vs. `FlyingSuperhero` (flying-specific).



# QUESTION 2.

#  Polymorphism Challenge:

## What It Does

This Python program shows **polymorphism** using a `Vehicle` base class and two subclasses, `Car` and `Plane`. Each class has a `move()` method that works differently: a generic vehicle moves, a car drives, and a plane flies. It uses Object-Oriented Programming (OOP) to make the code reusable and clear.

## Classes Explained

1. **Vehicle Class** (Basic Vehicle):

   - **Data**: `_name` (e.g., "Generic Vehicle"), protected with `_` for encapsulation.
   - **Action**: `move()` says the vehicle is moving (e.g., "Generic Vehicle is moving.").

2. **Car Class** (Inherits from Vehicle):

   - **Data**: Uses `_name` from Vehicle (e.g., "Toyota").
   - **Action**: `move()` says the car is driving (e.g., "Toyota is driving on the road 🚗.").

3. **Plane Class** (Inherits from Vehicle):

   - **Data**: Uses `_name` from Vehicle (e.g., "Boeing 747").
   - **Action**: `move()` says the plane is flying (e.g., "Boeing 747 is flying in the sky ✈️.")

## Why It Matters

- **Polymorphism**: The `move()` method works differently for each class (generic, driving, flying).
- **Inheritance**: `Car` and `Plane` reuse code from `Vehicle`.
- **Encapsulation**: `_name` is protected to control access.

## Notes

- Code to for OOP and polymorphism.
- Uses `_` to mark data as protected (Python convention).
- Test code shows how each class behaves differently with `move()`.
