import numpy as np;
import matplotlib.pyplot as plt;

def inputInt(prompt):
    while True:
        try:
            return int(input(prompt));
        except:
            print("Error: Please enter an integer");

def inputFloat(prompt):
    while True:
        try:
            return float(input(prompt));
        except:
            print("Error: Please enter a valid number");

def menu(prompt, options):
    print(prompt);
    count = 1;
    for i in options:
        print(str(count) + ") " + i);
        count += 1;
    while True:
        choice = inputInt("Choice: ")-1;
        if(choice >= 0 and choice <= len(options)):
           print("You Chose: " + options[choice]);
           return options[choice];
        else:
           print("Error: Please enter a valid number");

class wave:
    def __init__(self, frequency, amplitude, phase):
        self.type = "wave"
        self.frequency = frequency;
        self.amplitude = amplitude;
        self.phase = phase;
        self.functionNonVector = lambda x: amplitude*np.sin(2*np.pi*(x*frequency - phase)); #Actual piece of physics #1
        self.function = np.vectorize(self.functionNonVector);

class superimposition:
    def __init__(self, wave1, wave2):
        self.type = "superimposition";
        self.wave1 = wave1;
        self.wave2 = wave2;
        self.functionNonVector = lambda x: objects[wave1].function(x) + objects[wave2].function(x);
        self.function = np.vectorize(self.functionNonVector);

def inputNewObject(prompt):
    while True:
        choice = input(prompt);
        if choice in objects:
            print("Error: Please enter an unused name");
        else:
            return choice;

def inputExistingWave(prompt):
    while True:
        choice = input(prompt);
        if choice in objects:
            if objects[choice].type == "wave":
                return choice;
        else:
            print("Error: Please enter the name of an existing object");

global objects;
objects = dict(); #an array in which all of the waves are held

while True:
    menuChoice= menu("What would you like to do?", ["Add a wave", "Add a superimposition", "View the graph"])

    if menuChoice == "Add a wave":
        waveName = inputNewObject("Name of new wave: ");
        frequency = inputFloat("Frequency of wave (Hz): ");
        amplitude = inputFloat("Amplitude of wave (ratio)");
        phase = inputFloat("Phase of the wave (degrees)")/360;
        objects[waveName] = wave(frequency, amplitude, phase);
        print("New wave added!");
    
    elif menuChoice == "Add a superimposition":
        superimpositionName = inputNewObject("Name of new superimposition: ");
        wave1Name = inputExistingWave("Name of first wave: ");
        wave2Name = inputExistingWave("Name of second wave: ");
        objects[superimpositionName] = superimposition(wave1Name, wave2Name)

    elif menuChoice == "View the graph":
        time = np.linspace(0,1, 500);
        for k,v in objects.items():
            if v.type == "wave" :
                amplitude = v.function(time);
                plt.plot(time, amplitude, label=k)
            if v.type == "superimposition":
                amplitude = v.function(time);
                plt.plot(time, amplitude, label=k);
        plt.legend();
        plt.show();
