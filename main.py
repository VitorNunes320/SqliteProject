import modules.metods as metods
import modules.sqlite as sqlite

# instânciando o menu
menu = metods.Menu()
banco = sqlite.Banco()
banco.createDataBase()

while 1:
    # exibindo o menu das tabelas
    option_tabelas = int(menu.show("tabelas"))
    while not (-1 < option_tabelas < 8):
        option_tabelas = int(menu.show("tabelas"))
	
    if option_tabelas == 0:
        banco.saveClose()
        break
	
    # exibindo o menu de ações
    option_action = int(menu.show(option_tabelas))
    while not (-1 < option_action < 8):
        option_action = int(menu.show(option_tabelas))

    if option_action == 0:
        banco.saveClose()
        break
    
    atributos = ""
    table = menu.getTable(option_tabelas)
    column = banco.getColumns(table)

    if option_action == 1:
        metods.clearTerminal()
        infos = menu.getInfos(table)
        banco.insertDefault(table, metods.convertToString(column), metods.convertToString(infos))

    elif option_action == 2:
        metods.clearTerminal()
        banco.selectDefault(table)
		
    elif option_action == 3:
        metods.clearTerminal()
        if banco.selectDefault(table):
            id = int(input("\nDigite o id da linha que deseja atualizar: "))
            values = menu.getInfos(table)
            updates = menu.getUpdates(column, values)

            banco.updateDefault(table, metods.convertToString(updates), id)
    elif option_action == 4:
        metods.clearTerminal()
        if banco.selectDefault(table):
            id = int(input("\nDigite o id da linha que deseja deletar: "))
            banco.deleteDefault(table, id)
            banco.selectDefault(table)
    elif option_action == 5:
        metods.clearTerminal()
        banco.selectEspecial(table)
