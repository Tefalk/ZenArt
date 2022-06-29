# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define g = Character("Grandpa")

image bg orchid = "bg orchid copy.png"
image bg Bamboo = "bg Bamboo copy.png"
image bg Chryst = "bg Chryst copy.png"
image bg Plum = "bg Plum copy.png"
image bg Joshua1 = "bg JoshuaTree1 copy.png"
image bg Joshua4 = "bg JoshuaTree4 copy.png"
image Grandpa = "OldGuy2 copy.png"
image bg room = "bg japan.jpg"
image jt4 = "jt4.png"
image jt1 = "jt1.png"
image oldguy = "OldGuy2.png"

transform half_size:
    zoom 0.5

transform half_left:
    zoom 0.5,
    xalign .1

transform half_right:
    zoom 0.5,
    xalign .9

label oldguy:
    text "oldguy"
    return


# The game starts here.

label start:

    screen photo_menu():
        vbox xalign 0.5 yalign 0.5:
          #imagebutton auto "save_%s.png" action ShowMenu('save')
          ##imagebutton auto "skip_%s.png" action Skip()
          #imagebutton auto "afm_%s.png" action Preference("auto-forward mode", "toggle")
          textbutton "Photos for Pages 5":
              action Notify ("this works")
          textbutton "Photos for Pages 6+":
               action Show ("photo_5")

    screen photo_5():
        pass



    # Show a background.

    scene bg room

    # This shows a character sprite.

    # show grandpa as narrator

    show Grandpa

    play sound "audio/Yugen-Emotional-Ethnic-Music.mp3" loop

    # These display lines of dialogue.

    g "I am here to introduce a Ren'Py project that contains zen art paintings by Aidan and his grandpa along with some supporting text. All artwork other than the introduction pages are original."

    g "The first four paintings come from the book: A Beginners's Guide to Sumi-E by Shozo Koike, with artistic license freely taken."

    g "While this book was an excellent source of information and instruction, the intention here is not to do direct copies, but rather an intergenerational interpretation. No disrespect intended."

    g "The ZenBrush3 app on an Ipad Pro was used for painting. Thanks to Steve Elliot for his YouTube tutorials."


    scene bg orchid with fade

    "Page 1 is The Orchid. It is one of the noble gentlemen. Use the H key to dismiss the dialogue box."

    scene bg Bamboo with fade

    "Page 2 is Bamboo. It is another of the noble gentlemen. Use the H key to dismiss the dialogue box"

    scene bg Chryst with fade

    "Page 3 is Chrysanthemum. It is another of the noble gentlemen. Use the H key to dismiss the dialogue box"

    scene bg Plum with fade

    "Page 4 is Plum. It is the last of the noble gentlemen. Use the H key to dismiss the dialogue box"

    scene bg Joshua1 with fade

    "Page 5 is from the Joshua Tree National Park in California, USA. Use the H key to dismiss the dialogue box"

    scene bg Joshua4 with fade

    "Page 6 is from the Joshua Tree National Park in California, USA. Use the H key to dismiss the dialogue box"

    scene bg room

    "Page 7 has original photos from Joshua Tree National Park"

    show jt1 at half_left
    show jt4 at half_right

    call screen photo_menu()

    "Right now the links are hard to see"
