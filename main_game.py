import random

from colorama import Fore, Back, Style, init
from sty import fg, bg, ef, rs
from rich.console import Console
from rich.panel import Panel
from rich.table import Table


# Initialize Colorama
init(autoreset=True)

# Rich console
console = Console()


# ============================================================
# RANDOM COLOR THEME
# ============================================================

color_themes = [
    {
        "primary": Fore.CYAN,
        "secondary": Fore.YELLOW,
        "success": Fore.GREEN,
        "error": Fore.RED,
        "info": Fore.BLUE
    },
    {
        "primary": Fore.MAGENTA,
        "secondary": Fore.CYAN,
        "success": Fore.GREEN,
        "error": Fore.RED,
        "info": Fore.YELLOW
    },
    {
        "primary": Fore.BLUE,
        "secondary": Fore.LIGHTMAGENTA_EX,
        "success": Fore.LIGHTGREEN_EX,
        "error": Fore.LIGHTRED_EX,
        "info": Fore.CYAN
    },
    {
        "primary": Fore.LIGHTYELLOW_EX,
        "secondary": Fore.LIGHTCYAN_EX,
        "success": Fore.LIGHTGREEN_EX,
        "error": Fore.LIGHTRED_EX,
        "info": Fore.LIGHTMAGENTA_EX
    }
]

# Select a random theme every time the program starts
theme = random.choice(color_themes)

PRIMARY = theme["primary"]
SECONDARY = theme["secondary"]
SUCCESS = theme["success"]
ERROR = theme["error"]
INFO = theme["info"]


# ============================================================
# WELCOME SCREEN
# ============================================================

console.print()

console.print(
    Panel(
        "[bold cyan]🎯 NUMBER GUESSING GAME 🎯[/bold cyan]\n"
        "[yellow]Can you guess the secret number?[/yellow]",
        border_style="magenta",
        expand=False
    )
)

print()

print(f"{PRIMARY}Welcome to the Number Guessing Game!{Style.RESET_ALL}")

print(f"{SECONDARY}I am thinking of a number between 1 and 100.{Style.RESET_ALL}")

print(f"{INFO}You will have limited chances depending on difficulty.{Style.RESET_ALL}")

print()


# ============================================================
# RULES
# ============================================================

rules = Table(
    title="📜 Game Rules",
    border_style="cyan"
)

rules.add_column("Rule", style="yellow")
rules.add_column("Description", style="green")

rules.add_row("1", "Guess a number between 1 and 100")
rules.add_row("2", "Choose your difficulty level")
rules.add_row("3", "You have limited chances")
rules.add_row("4", "You will receive higher/lower hints")
rules.add_row("5", "Guess correctly to win!")

console.print(rules)

print()


# ============================================================
# DIFFICULTY SELECTION
# ============================================================

difficulty_table = Table(
    title="🎮 Select Difficulty",
    border_style="magenta"
)

difficulty_table.add_column("Choice", style="cyan", justify="center")
difficulty_table.add_column("Difficulty", style="yellow")
difficulty_table.add_column("Chances", style="green", justify="center")

difficulty_table.add_row("1", "Easy", "10")
difficulty_table.add_row("2", "Medium", "5")
difficulty_table.add_row("3", "Hard", "3")

console.print(difficulty_table)

print()


choice = input(
    f"{PRIMARY}Enter your choice (1-3): {Style.RESET_ALL}"
)


# ============================================================
# SET DIFFICULTY
# ============================================================

if choice == "1":

    chances = 10
    difficulty = "Easy"

elif choice == "2":

    chances = 5
    difficulty = "Medium"

elif choice == "3":

    chances = 3
    difficulty = "Hard"

else:

    print(
        f"{ERROR}❌ Invalid choice! Please select 1, 2 or 3."
    )

    exit()


# ============================================================
# GAME START
# ============================================================

console.print()

console.print(
    Panel(
        f"[bold green]Difficulty:[/bold green] {difficulty}\n"
        f"[bold yellow]Chances:[/bold yellow] {chances}\n\n"
        "[cyan]Let's start the game! 🎮[/cyan]",
        title="🚀 GAME START",
        border_style="green",
        expand=False
    )
)

# Generate random number
number = random.randint(1, 100)

attempts = 0


# ============================================================
# MAIN GAME LOOP
# ============================================================

while attempts < chances:

    print()

    try:

        guess = int(
            input(
                f"{PRIMARY}🎯 Enter your guess (1-100): "
                f"{Style.RESET_ALL}"
            )
        )

    except ValueError:

        print(
            f"{ERROR}❌ Please enter a valid number!"
        )

        continue


    # Validate range

    if guess < 1 or guess > 100:

        print(
            f"{ERROR}⚠️ Please enter a number between 1 and 100."
        )

        continue


    # Count valid attempt

    attempts += 1


    # ========================================================
    # CORRECT GUESS
    # ========================================================

    if guess == number:

        console.print()

        console.print(
            Panel(
                f"[bold green]🎉 CONGRATULATIONS! 🎉[/bold green]\n\n"
                f"You guessed the correct number: "
                f"[bold yellow]{number}[/bold yellow]\n\n"
                f"Attempts: [bold cyan]{attempts}[/bold cyan]\n"
                f"Difficulty: [bold magenta]{difficulty}[/bold magenta]",
                title="🏆 YOU WIN!",
                border_style="green",
                expand=False
            )
        )

        break


    # ========================================================
    # GUESS TOO LOW
    # ========================================================

    elif guess < number:

        print(
            f"{INFO}⬆️ Incorrect! "
            f"The number is greater than {guess}.{Style.RESET_ALL}"
        )


    # ========================================================
    # GUESS TOO HIGH
    # ========================================================

    else:

        print(
            f"{ERROR}⬇️ Incorrect! "
            f"The number is less than {guess}.{Style.RESET_ALL}"
        )


    # ========================================================
    # REMAINING CHANCES
    # ========================================================

    remaining = chances - attempts

    if remaining > 0:

        print(
            f"{SECONDARY}💡 Chances remaining: "
            f"{remaining}{Style.RESET_ALL}"
        )


# ============================================================
# GAME OVER
# ============================================================

else:

    console.print()

    console.print(
        Panel(
            f"[bold red]😔 GAME OVER[/bold red]\n\n"
            f"You used all {chances} chances.\n\n"
            f"The correct number was: "
            f"[bold yellow]{number}[/bold yellow]\n\n"
            f"Better luck next time! 🍀",
            title="💀 GAME OVER",
            border_style="red",
            expand=False
        )
    )


# ============================================================
# FINAL MESSAGE
# ============================================================

print()

# Using STY here
print(
    fg.li_cyan
    + ef.bold
    + "Thanks for playing! 🎮"
    + rs.all
)

print(
    bg.li_blue
    + fg.white
    + "Come back and try again!"
    + rs.all
)

print()
