"""Initial commit.

Revision ID: dba407c1663c
Revises: 3bba77ba57a5
Create Date: 2023-05-08 11:40:54.609056

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "dba407c1663c"
down_revision = "3bba77ba57a5"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("rounds", sa.Column("package_uuid", sa.Uuid(), nullable=True))
    op.drop_constraint("rounds_game_uuid_fkey", "rounds", type_="foreignkey")
    op.create_foreign_key(None, "rounds", "packages", ["package_uuid"], ["uuid"])
    op.drop_column("rounds", "game_uuid")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("rounds", sa.Column("game_uuid", sa.UUID(), autoincrement=False, nullable=False))
    op.drop_constraint(None, "rounds", type_="foreignkey")
    op.create_foreign_key("rounds_game_uuid_fkey", "rounds", "games", ["game_uuid"], ["uuid"])
    op.drop_column("rounds", "package_uuid")
    # ### end Alembic commands ###
