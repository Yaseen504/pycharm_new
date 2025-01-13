from utilities import clear_terminal, display_text, press_enter_arrow


def prologue():
    clear_terminal()

    print("|Prologue: Jerry one day in this bedroom|")
    print("----------------------------------------")
    press_enter_arrow()

    prologue_text = """
    Jerry: Joy, I don't get the concept of that at all.
    Every day just feels the exact same.
    I go to school, sit alone at lunch with no one, and watch TV.
    I feel like I'm drowning in a lake of dullness.
    Void of color, like the sky on a foggy day.
    My life is like, a dandelion, wishing to slowly dwindle away.
    The only thing I want is for this aching pain to go away."""

    display_text(
        text=prologue_text,
        lines_per_chunk=2,  # Display 2 lines at a time
        font_type="italics",  # Style: "italics"
        color=(255, 255, 255),  # Color: light blue
        delay=0.02,  # 0.05-second delay between characters
    )
