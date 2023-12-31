"""Create initial migration for post table

Revision ID: 67ae58146fd2
Revises: 
Create Date: 2023-10-24 22:17:46.179332

"""
from typing import Sequence, Union

import sqlalchemy as sa
import sqlmodel

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "67ae58146fd2"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("author")
    op.drop_table("post")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "post",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("title", sa.VARCHAR(), nullable=False),
        sa.Column("subtitle", sa.VARCHAR(), nullable=True),
        sa.Column("content", sa.VARCHAR(), nullable=False),
        sa.Column("views", sa.INTEGER(), nullable=False),
        sa.Column("author_id", sa.INTEGER(), nullable=True),
        sa.Column("date_created", sa.DATETIME(), nullable=True),
        sa.ForeignKeyConstraint(
            ["author_id"],
            ["author.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "author",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("first_name", sa.VARCHAR(), nullable=False),
        sa.Column("last_name", sa.VARCHAR(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###
