import random
from logging import getLogger

error_logger = getLogger("error")

uppercase_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_chars = uppercase_chars.lower()
digits_chars = "0123456789"
symbols = "()[]{};:-_/\\?+*#=&%@|"


class PasswordGenerationException(Exception):
    """Custom exception class for password generation"""

def _generate(population, length) -> str:
    """Generates the password suggestion with two possible methods depending on required suggestion length and the size of the population"""
    if len(population) >= length:
        return "".join(random.sample(population, length))
    else:
        return "".join(random.choices(population, k=length)) 

def _assemble_population(
        lowercase: bool,
        uppercase: bool,
        digits: bool,
        special: bool,
        ) -> str:
    """ Assembles the population to sample a password suggestion from"""
    
    population: str = ""
    
    if lowercase:
        population += lowercase_chars
    if uppercase:
        population += uppercase_chars
    if digits:
        population += digits_chars
    if special:
        population += symbols

    if len(population) == 0:
        exception = PasswordGenerationException("Cannot generate password from empty set of possible characters!")  
        error_logger.error(exception)
        raise exception

    return population
    

def generate(
        length: int = 12, 
        lowercase: bool = True, 
        uppercase: bool = True, 
        digits: bool = True, 
        special: bool = True, 
        ) -> str:
    """This function generates a password suggestion based on the input parameters"""
    
    if length <= 0:
        exception = PasswordGenerationException("Cannot generate password with 0 or negative length!")
        error_logger.error(exception)
        raise exception

    population = _assemble_population(
            lowercase,
            uppercase,
            digits,
            special,
            )

    return _generate(population, length)
