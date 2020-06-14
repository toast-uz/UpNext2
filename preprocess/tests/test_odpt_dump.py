'''
A test module for UpNext
Copyright(c) 2020 Tatsuzo Osawa
All rights reserved. This program and the accompanying materials
are made available under the terms of the MIT License:
    https: // opensource.org/licenses/mit-license.php
'''

from preprocess.src import odpt_dump
import pytest
import requests

http404_msg = '404 Not Found'


def _mock_response(mocker, is_normal):
    mock_resp = mocker.Mock()
    mock_resp.raise_for_status = mocker.Mock()
    if not is_normal:
        mock_resp.raise_for_status.side_effect = requests.exceptions.HTTPError(
            http404_msg)
    mock_resp.status_code = 200 if is_normal else 404
    mock_resp.content = b'TEST'
    return mock_resp


@pytest.mark.parametrize('is_normal', [
    True,
    False,
])
def test_get_and_save(mocker, is_normal):
    mock_resp = _mock_response(mocker, is_normal)
    mocker.patch('requests.get').return_value = mock_resp

    mock_file = mocker.mock_open()
    mocker.patch('builtins.open', mock_file)

    with pytest.raises(Exception) as e:
        odpt_dump.get_and_save('Dummy')
        raise

    if (not is_normal) and (str(e.value) is http404_msg):
        return

    assert mock_file.call_count == 1
    assert mock_file().write.call_args[0][0] == mock_resp.content


if __name__ == '__main__':
    pytest.main(['-v', __file__])
