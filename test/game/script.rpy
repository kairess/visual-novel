# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
image asuka = "asuka_1.png"
image asuka wink = "asuka_2.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('아스카', color="#c8ffc8")


# 여기에서부터 게임이 시작합니다.
label start:
    scene bg robot
    show asuka at left
    with dissolve

    e "새로운 렌파이 게임을 만들었군요."

    show asuka wink
    with dissolve

    e "이야기와 그림, 음악을 더하면 여러분의 게임을 세상에 배포할 수 있어요!"

    menu:
        "It's a videogame.":
            jump game
        "It's an interactive book.":
            jump book

    return

label game:
    e "It's a kind of videogame you can play on your computer or a console."
    jump marry

label book:
    e "It's like an interactive book that you can read on a computer or a console."
    jump marry

label marry:
    "And so, we become a visual novel creating duo."