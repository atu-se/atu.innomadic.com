---
title: DSA Lecture
subtitle: 11. Graphs
date: April 10, 2019
export_on_save:
  pandoc: true
output:
  custom_document:
    path: lecture11-slides.html
    pandoc_args: ["-t", "revealjs", "-V",  "revealjs-url=../../../presentation/reveal.js", "-V", "theme=beige", "--slide-level=2", "--standalone", "--katex=../../../presentation/katex/"]
---


# Objectives

* To model real-world problems using graphs and explain the Seven Bridges of Königsberg problem (§28.1).
* To describe the graph terminologies: vertices, edges, simple graphs, weighted/unweighted graphs, and directed/undirected graphs (§28.2).
* To represent vertices and edges using lists, edge arrays, edge objects, adjacency matrices, and adjacency lists (§28.3).
* To model graphs using the Graph interface, the AbstractGraph class, and the UnweightedGraph class (§28.4).
* To display graphs visually (§28.5).
* To represent the traversal of a graph using the AbstractGraph.Tree
class (§28.6).
* To design and implement depth-first search (§28.7).
* To solve the connected-circle problem using depth-first search (§28.8).
* To design and implement breadth-first search (§28.9).
* To solve the nine-tail problem using breadth-first search (§28.10).

# Introduction

## Introduction

Many real-world problems can be solved using graph algorithms.

## Introduction

* Graph problems are often solved using algorithms.

## Introduction

### Graph Algorithm Applications

* computer science
* mathematics
* biology
* engineering
* economics
* genetics
* social sciences.

## Introduction

### Algorithms in This Chapter

* depth-first search
* breadth-first search

### Algorithms in Next Chapter

* minimum spanning tree
* shortest paths in weighted graphs
