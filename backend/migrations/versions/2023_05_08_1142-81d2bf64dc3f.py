"""Initial commit.

Revision ID: 81d2bf64dc3f
Revises: dba407c1663c
Create Date: 2023-05-08 11:42:02.062877

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "81d2bf64dc3f"
down_revision = "dba407c1663c"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("rounds", "package_uuid", existing_type=sa.UUID(), nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("rounds", "package_uuid", existing_type=sa.UUID(), nullable=True)
    # ### end Alembic commands ###
