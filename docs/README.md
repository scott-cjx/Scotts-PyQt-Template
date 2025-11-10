# Scotts Python GUI Template

This is a template repo, meant to quicken the process of creating PyQT applications


## Installation

Typically, Python projects have their own virtual environments, either `Conda` or `venv` based. Regardless, with the virtual environment activated,

``` sh
pip install -e .
```

When this project is used as a submodule in another python project, create a `requirements.txt` with this project's environment added

<table>
<tr>
<th>Template</th>
<th>Example</th>
</tr>
<tr>
<td>

``` bash
-e .
-e <relative-path to this submodule>
```

</td>
<td>

``` bash
-e .
-e src/scotts-pyqt-template
```

</td>

</tr>
</table>