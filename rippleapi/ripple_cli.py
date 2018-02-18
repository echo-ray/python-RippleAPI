import click

from ripple import RippleClient

class State(object):
    '''
    Dummy class to store state attributes
    '''
    pass


@click.group()
@click.option('--debug/--no-debug', is_flag=True, default=False)
@click.option('--test-net', is_flag=True, default=True)
@click.pass_context
def cli(ctx, debug, test_net):
    ctx.obj = State()
    if test_net:        
        ctx.obj.server =  TEST_SERVER


@cli.command()
@click.argument('account')
@click.pass_context
def account_info(ctx, account):
    client = RippleClient(ctx.obj.server)
    resp = client.account_info(account)
    print(resp)


@cli.command()
@click.argument('account')
@click.pass_context
def account_tx(ctx, account):
    client = RippleClient(ctx.obj.server)
    resp = client.account_tx(account)
    print(resp)
    

if __name__ == '__main__':
    cli(obj={})

