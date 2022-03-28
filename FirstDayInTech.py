#
# firstdayintech.py
#
# Orignally inspired by  the Trapped in a cabin with Lord Byron simulator/RPG.
# Original concept and rules by Oliver Darkshire: Henry Sotherans, LTD.
# Orignal code by Imaginos the Quantum Magician 20220326
# Make sure to pip rich

import random
from rich.console import Console
from time import sleep

console = Console(color_system="truecolor")

failures = 0
success = 0
stress = 0
fakeresume = 0
last_happened = 0

# Let the user know what they're in for.
console.print("")
console.print(":white_exclamation_mark: [bold green]First Day in Tech[/bold green]:white_exclamation_mark:")
console.print("")
sleep(1)

console.print("You are new to Tech,:computer:")
sleep(0.50)

console.print("You hear there are great things to learn AND")
sleep(0.50)
console.print("Every role pays $100K+...:moneybag:")
console.print("")
sleep(1)
console.print("BUT...can you survive one day in Tech:question::question::question:")
console.print("")
sleep(1)


# When either failures, success, or stress hits 10, the game is over
while ((failures < 10) and (success < 10) and (stress < 10)):
    # See what Tech event is next
    # 1-2 Tech Projects, 3-4 Tech Drama, 5-6 Tech Community
    what_happened = random.randint(1, 6)
    event = random.randint(1, 6)
    if (what_happened == 6):
        fakeresume += 1
        if (fakeresume == 3):
            console.print("")
            console.print(":eyes: [bold red]You used a fake resume![/bold red] :eyes:")
            console.print("")
            console.print("Your job found out and now you are out of a job and the cash you spent :cry:")
            console.print("You're Failures, Success, and Stress has been reset to zero...")
            console.print("In essence, you just went back in time! :recycle:")
            console.print("")
            console.print("[bold green]You are now a cautionary tale. But there is always a chance for redemption![/bold green] :sparkles:")
            console.print("")
            failures = 0
            success = 0
            stress = 0
            fakeresume = 0
            sleep(5)
    else:
        # Had a non-6, reset disaster count
        fakeresume = 0
    if (what_happened < 3):
        # Tech Projects
        sleep(3)
        console.print(":notebook:Tech Projects:", end="\t")
        if (event == 1):
            console.print("[bold purple]You are the SME on something you know nothing about.[/bold purple]")
            stress += 1
        elif (event == 2):
            console.print("[bold purple]Someone takes credit for your work.[/bold purple]")
            success -= 1
        elif (event == 3):
            console.print("[bold purple]You get told to transition off the project you started.[/bold purple]")
            stress -= 1
            failures += 1
        elif (event == 4):
            console.print("[bold purple]You mistakenly blocked all DNS traffic in your network.[/bold purple]")
            failures += 2
        elif (event == 5):
            console.print("[bold purple]A new Microsoft Zero-Day drops on a Friday.[/bold purple]")
            stress += 1
        else:
            console.print("[bold purple]Your plan for staff, tech, culture improvements are implemented.[/bold purple]")
            stress -= 1
            success += 2
    elif (what_happened < 5):
        # Tech Drama
        sleep(3)
        console.print(":weary:Tech Drama:    ", end="\t")
        if (event == 1):
            console.print("[bold bright_cyan]Mgmt. says you have to turn your camera on during chats.[/bold bright_cyan]")
            stress += 1
        elif (event == 2):
            console.print("[bold bright_cyan]Mgmt. says you might need to return to the office.[/bold bright_cyan]")
            stress += 2
        elif (event == 3):
            console.print("[bold bright_cyan]80% of your team quit in the past month.[/bold bright_cyan]")
            stress += 3
        elif (event == 4):
            console.print("[bold bright_cyan]Your company is not giving any raises, again.[/bold bright_cyan]")
            failures += 1
        elif (event == 5):
            console.print("[bold bright_cyan]Your boss shoots down your prototype/project idea.[/bold bright_cyan]")
            failures += 2
        else:
            console.print("[bold bright_cyan]No one on your team gives you credit for your ideas.[/bold bright_cyan]")
            stress += 2
    else:
        # Tech Community
        sleep(3)
        console.print(":gift:Tech Community:", end="\t")
        if (event == 1):
            console.print("[bold chartreuse2]You support and take part in local conferences/groups.[/bold chartreuse2]")
            success += 1
        elif (event == 2):
            console.print("[bold chartreuse2]You get sponsored for a training scholarship.[/bold chartreuse2]")
            stress -= 1
            success += 1
        elif (event == 3):
            console.print("[bold chartreuse2]You don't find ways to help those coming up in tech.[/bold chartreuse2]")
            failures += 1
        elif (event == 4):
            console.print("[bold chartreuse2]People ask you to be their mentor every day.[/bold chartreuse2]")
            failures += 1
            success += 1
        elif (event == 5):
            console.print("[bold chartreuse2]You don't spend the time building your network.[/bold chartreuse2]")
            success -= 1
        else:
            console.print("[bold chartreuse2]You share helpful info to others.[/bold chartreuse2]")
            success += 1

console.print("")
sleep(3)
if (failures >= 10):
    console.print("[bold yellow]You are no longer fit to call yourself a 10X Engineer![/bold yellow] :pensive:")
elif (success >= 10):
    console.print("[bold blue]You are now looked upon with greater attention and admiration...[/bold blue] :+1:")
    console.print("[bold blue]Thus inviting greater future stress and failures.[/bold blue] :grimacing:")
else:
    console.print("[bold green]You take what little vested options you have...[/bold green] :money_with_wings:")
    console.print("[bold green]And finally move to that farm in the country that all tech folks talk about.[/bold green] :house_with_garden:")
