from fileClass import Config


class Strategy:
    def __init__(self, player, adv, dna, nrodadas, dano, vitorias, derotas):
        self.player = player
        self.adv=adv
        #DNA
        self.DNA = dna
        #Fenótipo
        self.rodadas = nrodadas
        self.damage = dano
        self.vitorias = vitorias
        self.derotas = derotas
        self.apontador = -1

    def getProtein(self):
        """
        Realizar um get para cada jogada de Strategy.
            -Se a estratégia ultrapassar o numero previsto de jogadas ele retona -1
        :return: int
        """
        if self.apontador > self.rodadas:
            return -1
        self.apontador += 1
        return self.DNA[self.apontador]

    def sumDamage(self, damage):
        self.damage += damage

    def addProtein(self, jogada):
        self.DNA += jogada

    def contRound(self):
        self.rodadas += 1

    def toCompare(self, strategy):
        """
        Se a minha estratégia é melhor que a outra
        :param strategy:
        :return: boolean
        """
        if self.damage > strategy.damege and self.rodadas < strategy.rodadas:
            return True
        return False

    def equals(self,strategy):
        """
        Se ela é igual a outra
        :param strategy:
        :return: boolean
        """
        if self.DNA == strategy.DNA or strategy.DNA in self.DNA :
            return True
        return False


class DAOStrategy:
    def __init__(self):
        self.TXT = "Mind.txt"

    def addStrategy(self, strategy):
        """
        :param strategy: Strategy
        :return: void
        """
        infoStrategy = f"{strategy.player}-{strategy.adv}-{strategy.DNA}-{strategy.rodadas}-{strategy.damage}-{strategy.vitorias}-{strategy.derotas}"
        arq = open(self.TXT, 'r')
        conteudo = arq.readlines()
        conteudo.append(infoStrategy)

        arq = open(self.TXT, 'w')
        arq.writelines(conteudo)
        arq.close()

    def getStrategy(self, namePlayer, nameAdv):
        arq = open(self.TXT, 'r')
        conteudo = arq.readlines()
        for infoStrategy in conteudo:
            listInfo = infoStrategy.split("-")
            if listInfo[Config["namePlayer"]] == namePlayer and listInfo[Config["nameAdv"]] == nameAdv:
                arq.close()
                return Strategy(listInfo[Config["namePlayer"]], listInfo[Config["nameAdv"]], listInfo[Config["DNA"]],
                                listInfo[Config["nRodadas"]], listInfo[Config["damage"]], listInfo[Config["vitorias"]],
                                listInfo[Config["derotas"]])
        arq.close()
        return None


est = Strategy("Jhonatan", "Jhean", "01110111", 5, 500, 0, 0)
dao = DAOStrategy()
print(dao.getStrategy("Jhonatan","Jhean").DNA)