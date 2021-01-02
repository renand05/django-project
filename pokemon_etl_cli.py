import click
import bonobo
import pokebase as pb

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

conn_url = 'postgres://postgres:postgres@localhost:5432/postgres'
engine = create_engine(conn_url)
session = scoped_session(sessionmaker(bind=engine))

class Pokemon(Base):
    __tablename__: str = "pokeapi_pokemon"

    id = Column(String, primary_key=True)
    name = Column(String)
    height = Column(Integer)
    weight = Column(Integer)

def extract(evolution_chain_id):
    evolution_chain = pb.APIResource('evolution-chain', int(evolution_chain_id))
    pokemon = pb.APIResource("pokemon", evolution_chain.chain.species.name)
    yield {"evolution-chain": evolution_chain, "pokemon": pokemon}

def transform(*args):
    data = args[0]
    yield Pokemon(
        id=data["pokemon"].id,
        name=data["pokemon"].name,
        height=data["pokemon"].height,
        weight=data["pokemon"].weight)

def load(*args):
    data = args[0]
    try:
        session.add(data)
        session.commit()
    except error as E:
        print(E)

def get_graph(**options):
    graph = bonobo.Graph()
    graph.add_chain(extract(options["evolution_chain_id"]), transform, load)

    return graph

@click.command()
@click.option('--evolution_chain_id', prompt='Id of pokemon evolution-chain',
              help='The pokemon evolution-chain id.')
def pokemon_etl_by_id(evolution_chain_id):
    parser = bonobo.get_argument_parser()
    with bonobo.parse_args(parser) as options:
        bonobo.run(
            get_graph(evolution_chain_id=evolution_chain_id),
            services={}
        )

if __name__ == '__main__':
    pokemon_etl_by_id()
