from typing import Callable

def generator_numbers(text: str):
    # Split text into words
    words = text.split()
    for i, word in enumerate(words):
        try:
            #check if the number isn't at the beginning or end of the text
            if i > 0 and i < len(words) - 1:
                yield float(word)
        except ValueError:
            continue

#Calculates total income using a number generator
def sum_profit(text: str, func: Callable[[str], float]) -> float:
    return sum(func(text))

#Usage example
if __name__=="__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income:.2f}")