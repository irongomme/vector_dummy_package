#!/usr/bin/env python3

import anki_vector

args = anki_vector.util.parse_command_args()

with anki_vector.Robot(args.serial) as robot:
    robot.say_text('Hey Vector !')
