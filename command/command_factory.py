from command import command

def command_factory(name, ma=0, ol=[None]):
    return lambda *args, **kwargs: command(name, max_args=ma, option_list=ol, 
                                           arguments=args, options=kwargs)

