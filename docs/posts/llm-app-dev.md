---
title: '大语言模型应用开发实战：从概念到落地'
date: '2025-01-05'
summary: '详细介绍如何使用 LangChain 和 OpenAI API 构建智能应用，包含完整代码示例'
tags: ['LLM', 'LangChain', 'AI']
---

# 大语言模型应用开发实战

大语言模型（LLM）已经成为 AI 应用开发的核心技术。本文将详细介绍如何使用 LangChain 和 OpenAI API 构建智能应用。

## 一、环境准备

首先安装必要的依赖：

```bash
pip install langchain openai python-dotenv
```

## 二、基本配置

创建 `.env` 文件：

```bash
OPENAI_API_KEY=your-api-key
```

## 三、简单问答应用

```python
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(temperature=0.7, openai_api_key=os.getenv("OPENAI_API_KEY"))

template = """
你是一个资深的 Python 开发者，请回答以下问题：

问题：{question}

答案：
"""

prompt = PromptTemplate(template=template, input_variables=["question"])
chain = LLMChain(llm=llm, prompt=prompt)

result = chain.run("什么是装饰器模式？")
print(result)
```

## 四、文档问答系统

```python
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

loader = TextLoader("documents/tech_doc.txt")
index = VectorstoreIndexCreator().from_loaders([loader])

query = "文档中提到的最佳实践有哪些？"
result = index.query(query)
print(result)
```

## 五、多步骤工作流

```python
from langchain.chains import SequentialChain

template1 = """
请将以下问题翻译成英文：{question}
"""

template2 = """
请用英文回答以下问题：{english_question}
"""

prompt1 = PromptTemplate(template=template1, input_variables=["question"])
chain1 = LLMChain(llm=llm, prompt=prompt1, output_key="english_question")

prompt2 = PromptTemplate(template=template2, input_variables=["english_question"])
chain2 = LLMChain(llm=llm, prompt=prompt2, output_key="answer")

overall_chain = SequentialChain(
    chains=[chain1, chain2],
    input_variables=["question"],
    output_variables=["english_question", "answer"]
)

result = overall_chain({"question": "什么是机器学习？"})
print(result["answer"])
```

## 六、总结

通过以上示例，你已经学会了如何使用 LangChain 构建各种 LLM 应用。关键要点：

1. 选择合适的提示词模板
2. 合理设置温度参数
3. 使用链（Chain）组合多个步骤
4. 结合向量数据库处理文档

> 实践是最好的老师，动手尝试构建自己的 AI 应用吧！
