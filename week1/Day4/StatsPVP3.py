"""PVP"""
def main():
    """StartPVP"""
    nameplayer_1 = input()
    hpplayer_1 = int(input())
    atlplayer_1 = int(input())
    defplayer_1 = int(input())
    nameplayer_2 = input()
    hpplayer_2 = int(input())
    atlplayer_2 = int(input())
    defplayer_2 = int(input())
    print('''##############
# '''+"%10s"%(nameplayer_1)+''' #
# HP:'''+("%7s"%("O"*hpplayer_1))+''' #
# ATk || DEF #
# '''+"%04d"%(atlplayer_1)+'''||'''+"%04d"%(defplayer_1)+''' #
############## VS ##############
                  # '''+"%10s"%(nameplayer_2)+''' #
                  # HP:'''+("%7s"%("O"*hpplayer_2))+''' #
                  # ATk || DEF #
                  # '''+"%04d"%(atlplayer_2)+'''||'''+"%04d"%(defplayer_2)+''' #
                  ##############''')
main()
