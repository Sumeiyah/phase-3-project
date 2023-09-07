"""Initial migration

Revision ID: 16a272b4b0b5
Revises: fd79be6562d1
Create Date: 2023-09-07 22:12:03.331119

"""
from typing import Sequence, Union
from lib.database import Base
from alembic import op
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from lib.database import Student, Course, Grade


# revision identifiers, used by Alembic.
revision: str = '16a272b4b0b5'
down_revision: Union[str, None] = 'fd79be6562d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    engine = create_engine('sqlite:///student_grade_tracker.db')
    Base.metadata.bind = engine
    Base.metadata.create_all(bind=engine)


def downgrade() -> None:
    engine = create_engine('sqlite:///student_grade_tracker.db')
    Base.metadata.bind = engine
    Base.metadata.create_all(bind=engine)
