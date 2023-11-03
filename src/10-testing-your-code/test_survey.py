import pytest
from survey import AnonymousSurvey

# 测试需要的数据的初始化，这些数据可以被后面的测试函数共享
@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    
    # 返回了被测试类的对象
    return language_survey

def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response('English')
    # 断言'English'是否在被测试类的属性responses列表中
    assert 'English' in language_survey.responses


def test_store_three_responses(language_survey):
    """Test that three individual responses are stored properly."""
    responses = ['English', 'Spanish', 'Mandarin']
    # 用for循环去调用被测试类的方法store_response
    for response in responses:
        language_survey.store_response(response)

    # 用for循环去断言responses列表中的每个元素
    # 是否在被测试类的属性responses列表中
    for response in responses:
        assert response in language_survey.responses