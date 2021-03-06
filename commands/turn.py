import commands2
from wpimath.controller import PIDController
from constants import turn_K_p, turn_K_I, turn_K_D
from subsytems.drivetrain import Drivetrain
import math

ACCEPTABLE_ERROR = 10


class Turn(commands2.PIDCommand):
    # /**
    # * Creates a new DriveStraight.
    # */
    def __init__(self, distSetPt: float, drivetrain: Drivetrain):
        self.drivetrain = drivetrain
        super().__init__(
            PIDController(turn_K_p, turn_K_I,
                          turn_K_D),

            drivetrain.gyro.getYaw,

            distSetPt,

            drivetrain.turn,
            [drivetrain])

    def isFinished(self):
        print(self.drivetrain.gyro.getYaw(), self.getController().getSetpoint())
        return math.fabs(self.getController().getPositionError()) < ACCEPTABLE_ERROR

    def initialize(self) -> None:
        self.drivetrain.m_left_encoder.setPosition(0)
        self.drivetrain.m_right_encoder.setPosition(0)
        self.drivetrain.gyro.setYaw(0)
