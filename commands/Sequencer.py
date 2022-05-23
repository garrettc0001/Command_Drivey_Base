from subsytems.drivetrain import Drivetrain
import commands2
from commands.drivestraight import DriveStraight
import wpilib
import math
from commands.defaultDrive import DefaultDrive
from commands.turn import Turn


class Sequencer(commands2.SequentialCommandGroup):
    def __init__(self, drivetrain):
        self.drivetrain = drivetrain
        super().__init__()
        self.addCommands(
            drivetrain.driveStraight(5 * 12 / (4 * math.pi) * 360),
            drivetrain.turn(180),
            drivetrain.driveStraight(5 * 12 / (4 * math.pi) * 360),
            drivetrain.turn(180)
        )