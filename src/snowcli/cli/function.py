#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.dir_util import copy_tree
import os
from pathlib import Path
import pkg_resources
import typer

from snowcli.utils import conf_callback
from snowcli.cli.snowpark_shared import snowpark_create, snowpark_describe, snowpark_execute, snowpark_package, snowpark_update

app = typer.Typer()
EnvironmentOption = typer.Option("dev", help='Environment name', callback=conf_callback, is_eager=True)

@app.command("init")
def function_init():
    """
    Initialize this directory with a sample set of files to create a function.
    """
    copy_tree(pkg_resources.resource_filename(
        'templates', 'default_function'), f'{os.getcwd()}')

@app.command("create")
def function_create(environment: str = EnvironmentOption,
                    name: str = typer.Option(..., '--name', '-n',
                                             help="Name of the function"),
                    file: Path = typer.Option('app.zip',
                                              '--file',
                                              '-f', 
                                              help='Path to the file or folder to deploy',
                                              exists=True,
                                              readable=True,
                                              file_okay=True),
                    handler: str = typer.Option(...,
                                                '--handler',
                                                '-h',
                                                help='Handler'),
                    input_parameters: str = typer.Option(...,
                                                         '--input-parameters',
                                                         '-i',
                                                         help='Input parameters - such as (message string, count int)'),
                    return_type: str = typer.Option(...,
                                                    '--return-type',
                                                    '-r',
                                                    help='Return type'),
                    overwrite: bool = typer.Option(False,
                                                   '--overwrite',
                                                   '-o',
                                                   help='Replace if existing function')
                    ):
    snowpark_create(type='function', environment=environment, name=name, file=file, handler=handler, input_parameters=input_parameters, return_type=return_type, overwrite=overwrite)


@app.command("update")
def function_update(environment: str = EnvironmentOption,
                    name: str = typer.Option(..., '--name', '-n', help="Name of the function"),
                    file: Path = typer.Option('app.zip',
                                              '--file',
                                              '-f', 
                                              help='Path to the file to update',
                                              exists=True,
                                              readable=True,
                                              file_okay=True),
                    handler: str = typer.Option(...,
                                                '--handler',
                                                '-h',
                                                help='Handler'),
                    input_parameters: str = typer.Option(...,
                                                         '--input-parameters',
                                                         '-i',
                                                         help='Input parameters - such as (message string, count int)'),
                    return_type: str = typer.Option(...,
                                                    '--return-type',
                                                    '-r',
                                                    help='Return type'),
                    replace: bool = typer.Option(False, 
                                                '--replace-always', '-r', 
                                                help='Replace function, even if no detected changes to metadata')
                    ):
    snowpark_update(type='function', environment=environment, name=name, file=file, handler=handler, input_parameters=input_parameters, return_type=return_type, replace=replace)

@app.command("package")
def function_package():
    snowpark_package()

@app.command("execute")
def function_execute(environment: str = EnvironmentOption,
                     function: str = typer.Option(..., '--function', '-f', help='Function with inputs. E.g. \'hello(int, string)\'')):
    snowpark_execute(type='function', environment=environment, select=function)


@app.command("describe")
def function_describe(environment: str = EnvironmentOption,
                      name: str = typer.Option('', '--name', '-n', help="Name of the function"),
                      input_parameters: str = typer.Option('',
                                                         '--input-parameters',
                                                         '-i',
                                                         help='Input parameters - such as (message string, count int)'),
                      function: str = typer.Option('', '--function', '-f', help='Function signature with inputs. E.g. \'hello(int, string)\'')
                      ):
    snowpark_describe(type='function', environment=environment, name=name, input_parameters=input_parameters, signature=function)