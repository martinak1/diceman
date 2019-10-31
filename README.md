# diceman - A Discord bot for simulating dice rolls in tabletop games

![GitHub](https://img.shields.io/github/license/martinak1/diceman) ![Travis (.org)](https://img.shields.io/travis/martinak1/diceman)

<!--Add gif of IO-->

## Message Formating

    !d <Number of dice to roll>d<Sides on the dice> <First roll value><Qualifier> <Second roll value><Qualifier> ...

## Example

    # This simulates rolling 10 D6 with the requirements of the first roll being 
    # 4 up and then a 3 up for the second roll

    input msg: !d 10d6 4+ 3+  
    response msg: 4 successful rolls