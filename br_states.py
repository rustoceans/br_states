# coding: utf-8


class State(object):

    def __init__(self, uf=None):
        self.uf = uf

    STATES = (
        ('AC', u'Acre'),
        ('AL', u'Alagoas'),
        ('AP', u'Amapá'),
        ('AM', u'Amazonas'),
        ('BA', u'Bahia'),
        ('CE', u'Ceará'),
        ('DF', u'Distrito Federal'),
        ('ES', u'Espírito Santo'),
        ('GO', u'Goiás'),
        ('MA', u'Maranhão'),
        ('MT', u'Mato Grosso'),
        ('MS', u'Mato Grosso do Sul'),
        ('MG', u'Minas Gerais'),
        ('PA', u'Pará'),
        ('PB', u'Paraíba'),
        ('PR', u'Paraná'),
        ('PE', u'Pernambuco'),
        ('PI', u'Piauí'),
        ('RJ', u'Rio de Janeiro'),
        ('RN', u'Rio Grande do Norte'),
        ('RS', u'Rio Grande do Sul'),
        ('RO', u'Rondônia'),
        ('RR', u'Roraima'),
        ('SC', u'Santa Catarina'),
        ('SP', u'São Paulo'),
        ('SE', u'Sergipe'),
        ('TO', u'Tocantins'),
    )

    STATES_CODES = (
        ('AC', 12),
        ('AL', 27),
        ('AP', 16),
        ('AM', 14),
        ('BA', 29),
        ('CE', 23),
        ('DF', 53),
        ('ES', 32),
        ('GO', 52),
        ('MA', 21),
        ('MT', 50),
        ('MS', 50),
        ('MG', 31),
        ('PA', 15),
        ('PB', 25),
        ('PR', 41),
        ('PE', 26),
        ('PI', 22),
        ('RJ', 33),
        ('RN', 24),
        ('RS', 43),
        ('RO', 11),
        ('RR', 14),
        ('SC', 42),
        ('SP', 35),
        ('SE', 28),
        ('TO', 17),
    )

    def states(self):
        """ Return tuple of states

            state = State()
            state.states()
        """
        return self.STATES

    def description(self):
        """ Return description of specific state

            state = State('SP')
            state.description()
            >>> 'São Paulo'
        """
        return self.to_dict().get(self.uf)

    def codes(self):
        """ Return tuple of state codes

            state = State()
            state.codes()
        """
        return self.STATES_CODES

    def code(self):
        """ Return specific state code

            state = State('SP')
            state.code()
            >>> 35
        """
        return self.codes_dict().get(self.uf)

    def codes_dict(self):
        """ Return dict of state codes

            state = State()
            state.codes_dict()
        """
        return dict(self.STATES_CODES)

    def to_dict(self):
        """ Return tuple of states

            state = State()
            state.to_dict()
        """
        return dict(self.STATES)

    def full_description(self):
        """ Return full description of specific state

            state = State('SP')
            state.full_description()
            >>> 'SP - São Paulo'
        """
        return u'{uf} - {description}'.format(
            uf=self.uf, description=self.description())
