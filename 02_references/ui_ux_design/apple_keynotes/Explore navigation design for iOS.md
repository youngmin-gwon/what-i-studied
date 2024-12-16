---
title: Explore navigation design for iOS
tags: []
aliases: []
date modified: 2024-12-16 17:31:27 +09:00
date created: 2024-12-09 21:31:10 +09:00
---

## Navigation teaches people about
- how things behave
- where things belong
- how things work

## Goal of navigation
- to provide enough of a foundation of familiarity

## Focus and Intention
---
## Tab bars
- a global navigation tool that sits at the bottom of the screen
	- **categorizing** an app's content into different sections
### Guidelines
1. Use tabs to reflect your information hierarchy
2. Balance features throughout tabs
	- Do not put all functionalities in one tab
		- Users cannot help but scrolling to find what functionality they want to use
	- Ask yourself why people use your app: great apps have focused solutions
	- Part of designing great tab bars is organizing your contents
3. Avoid duplicating functionality into a single tab
	- Home tab or overview tab is a confusion
	- It may cause "tab-jump", a function of routing to a certain functionality, which is jarring and disorienting
4. Keep tabs persisent throughout your app
5. Use clear and concise labels
---
## Hierarchical navigation

### Ways to navigate between screens of an app

1. Push
	- directly reflect information hierarchy
	- an expected default when drilling further into an app's hierarchy
	- a literal representation of moving through content and drilling into details
2. Modal presentation
	- a self-contained task in an interface
		- self-contained?
			- simple task, multi-step, or full screen
	- this prevents people from drilling further into your app
		- intentional disruption because the purpose is the reinforce the focus
	- good for independent workflows
	- it creates focus by separating people from the information hierarchy

### Guidelines

#### 1. Hierarchical navigation
- Use a push transition to navigate between different levels of your app's hierarchy
	- Hierarchical navigation reinforces the relationship between top-level and secondary content
- Keep the tab bar anchored to the bottom of the screen
- Use the navigation bar to orient people
- Use with a disclosure indicator
- When navigating frequently between content

#### 2. Modal presentation
- Present from the bottom of the screen
- Use for a simple task, multi-step(to reinforce the focus), or full screen
- Dismiss a modal with 'cancel' and preferred actions
- Limit modals over modals
