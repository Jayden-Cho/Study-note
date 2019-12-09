**Unit 05 Objectives**

- Learn the concept and the application of computer simulations
  - Introduction production
- Objectives are
  - Understanding the concepts of modeling and simulation

# Comprehend a problem

**Real World Problems**

- Role of ISE?
  - Developing a specialized solution through science and engineering.
  - Developing a managerial solution through computational analyzes.
  - However, need to comprehend the problem first.

<br>

**How to Comprehend a Problem?**

- The way to comprehend a given program :
  - Estimate the outputs of a given input.
  - Estimate the progress of the program in the system.
  - Just as we traced the function calls of the recursion in the execution timeline.
- How to comprehend a problem?
  - Estimate the future of a given status-quo(상황).
  - Estimate the progress of problem factors in the system.
  - However, the real-world problem is not a program in a well-defined programming language.

- 문제가 주어졌다 치자. 어떻게 문제를 이해할까?

  - 주어진 입력에 대해 출력을 예측해 보는 것. 프로그램 자체를 이해했다는 배경을 전제하에.
  - 프로그램이 어떻게 돌아갈까에 대한 예상.

- 현재의 문제는 어떻게 이해할까?

  - 현재 상황(status-quo)으로 미래를 예측해보자.

  - 복잡한 시장이 있다고 치자. 옷에 대한 가격이 형성되있을 때 가격이 올라갈지 내려갈지 예측을 할 수 있다면 시장에 대해 이해했다고 생각할 수 있다.
  - 문제를 표현해야 한다. Fibonacci같은 경우는 이미 표현이 되었고, 시장은 수식으로 표현되지 않았다. 
    - 수식으로 표현하는 것 자체가 일이다. 
    - 표현으로 supply-demand curve를 생각할 수 있겠다.

- Fibonacci Sequence와 SDC의 같은 점은:
  - 두 문제가 존재한다.
  - 그것을 프로그램(모델)로 만들었다.
  - 프로그램을 execute해서 어떻게 돌아가는지 알아냈고, SDC의 solution을 찾았다.

- 다른 점은
  - 이미 표현된 문제(Fibonacci)와 표현되지 않은 문제(Supply-Demand)

<br>

# Introduction of Modeling

 **Models and Why Modeling?**

- Since, it is difficult to trace the real-world problems.
  - We create a model that simplifies the real-world problems.
    - The model is a simplification of the real-world problems.
    - The model is an essence of the real world problems.

- 현실의 문제는 따라가기(trace) 어렵다.
  - 어려운 현실을 간단화해 model을 만들어낸다.

- Why use montage? Not picture?
  - 우리가 주요하게 생각해야할 것을 강조해서 그린 그림.
- Antoine de Saint-Exupery
  - Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away. 더 이상 더할게 없을 때가 아니라 더 이상 뺄께 없을 때 완벽해진다.
    - 현실과 또옥같이 한다해도 분명 허점이 생긴다. 대신 핵심만 표현해서 더 이상 뺄 것이 없을 때가 완벽해지는 것이다. 
- What to remove?
  - What to leave in the model
  - What to remove from the real world
  - Determined by objectives. 분석의 목적에 따라.

<br>

**Two Types of Models**

- Models to solve :
  - Numerical modeling
    - Linear programming, Integer programming/
    - Goal: converting the real world problems into formula, then finding optimal solutions through solvers.
- Models to simulate :
  - System dynamics, discrete event models, agent based models.
    - Event graphs, petri-net, agent modeling.
    - Goal: approximating to the real world problems, then finding the optimal solutions through repetitive simulations.

- 시장을 이해하기 위해서 supply-demand curve를 만들고, 수학적으로 solution을 찾아냈다.
  - Supply-demand curve 자체가 모델. 이것은 numerical model. 
    - 현실의 문제를 formula로 표현하고 그 formula에 맞는 solution을 찾는 것. 

- 현실에 모두 풀수 있는 모델이 있는 것은 아니다.
  - 제조 분야에서 움직이는 것 하나하나 표현하는 것은 불가능.
  - 문제를 푼다기 보다는 simulate하는 것.

<br>

# Examples of Simulation

**Infectious Disease**

- SIR model(1925)
- A lifecycle of a patient
  - Susceptible
  - Infectious
  - Recovery
- More susceptible and infectious people
  - Infectious people increases
- After some time, infectious people get recovered
- This is a model without the loss of population
- See how to represent the interactions between infectious and susceptible populations

의료 분야의 예시.

- 병이 얼마나 심각한지 알아보는 model.
- 인구 상태를 표현. 
  - 병에 걸릴 수 있는 상태 - 병에 걸린 상태 - 회복 상태.

- 현실의 문제를 공식으로 만들고 그것을 프로그래밍한다.
- System dynamics라고 부름.

<br>

**Hospital Management**

- In hospitals
  - Patients go through
    - Waiting area
    - Exam room
    - Treatment room
    - Exit
  - These are a sequence of the patient care process.

이번에는 사람이 아닌 object.

- 매우 선형적임.
- Event의 단계에 따라 달라짐. 이런 것을 discrete event simulation이라고 한다.
  - 이전은 time을 handling. 
  - 큰 사이즈를 다룬다기 보다는 좀 더 소규모를 다룸.

<br>

**Airport Model**

- In airports
  - Passengers go through
    - Check-in computer
    - Security check, etc.
  - These are a sequence of airport travel process.

Discrete event를 정의하고 통계를 내면 관리 방법을 알 수 있게 된다.

- 어느 순서를 어떻게 배치할지, sequence를 어떻게 설정할지.
- 사람들의 진행 방향을 simulation해 최적의 결과를 얻어낸다.

<bR>

**Example : Traffice Network Modeling**

- Traffic
  - Agent : individual vehicles
  - Space : road network
- Problem 
  - No center control of agents
  - Agents choose their route based upon the latency from the selfish and rational perspective
  - Then, how to model and simulate this distributed traffic agent model?

교통 체증을 어떻게 모델링할 것인가? discrete event model.