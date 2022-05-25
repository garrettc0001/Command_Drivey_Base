import commands2
from wpimath.controller import PIDController
from constants import movement_K_p, movement_K_I, movement_K_D
from subsytems.drivetrain import Drivetrain
import math

ACCEPTABLE_ERROR = 10

class DriveStraight(commands2.PIDCommand):
    # /**
    # * Creates a new DriveStraight.
    # */
    def __init__(self, dist: float, drivetrain: Drivetrain):
        self.drivetrain = drivetrain
        distSetPt = dist * 12 / (4 * math.pi) * 360  # converts feet to ticks
        super().__init__(
            PIDController(movement_K_p, movement_K_I,
                          movement_K_D),

            self.drivetrain.m_left_encoder.getPosition,

            distSetPt,

            self.drivetrain.driveStraight,
            [drivetrain])

    def isFinished(self):
        print(self.drivetrain.m_left_encoder.getPosition(), self.getController().getSetpoint())
        return math.fabs(self.getController().getPositionError() < ACCEPTABLE_ERROR)

    def initialize(self) -> None:
        self.drivetrain.m_left_encoder.setPosition(0)
        self.drivetrain.m_right_encoder.setPosition(0)
