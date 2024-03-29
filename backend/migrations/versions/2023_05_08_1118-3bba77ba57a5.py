"""Initial commit.

Revision ID: 3bba77ba57a5
Revises: 504326e6180c
Create Date: 2023-05-08 11:18:48.111217

"""
from alembic import op
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "3bba77ba57a5"
down_revision = "504326e6180c"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "games", "started_at", existing_type=postgresql.TIMESTAMP(timezone=True), nullable=True
    )
    op.alter_column(
        "games", "finished_at", existing_type=postgresql.TIMESTAMP(timezone=True), nullable=True
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "games", "finished_at", existing_type=postgresql.TIMESTAMP(timezone=True), nullable=False
    )
    op.alter_column(
        "games", "started_at", existing_type=postgresql.TIMESTAMP(timezone=True), nullable=False
    )
    # ### end Alembic commands ###
