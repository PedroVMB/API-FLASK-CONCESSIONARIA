"""Initial migration

Revision ID: cd4626a8ad56
Revises: 
Create Date: 2023-09-03 21:07:45.625652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd4626a8ad56'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('veiculo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=50), nullable=False),
    sa.Column('cor', sa.String(length=50), nullable=False),
    sa.Column('marca', sa.String(length=100), nullable=False),
    sa.Column('modelo', sa.String(length=100), nullable=False),
    sa.Column('ano_fabricacao', sa.Integer(), nullable=False),
    sa.Column('estado', sa.String(length=50), nullable=False),
    sa.Column('km_rodados', sa.Float(), nullable=False),
    sa.Column('passagem_por_leilao', sa.String(length=3), nullable=False),
    sa.Column('formas_de_pagamento', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('veiculo')
    # ### end Alembic commands ###