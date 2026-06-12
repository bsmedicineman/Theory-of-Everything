#!/usr/bin/env python3
"""
THEORY OF EVERYTHING EQUATION SOLVER
With Persistent Reciprocal Identity (PRI) Framework
Sacred Geometry Integration & Sumerian Base-60 System
"""

import os
import re
import sys
import json
import math
import sympy
import networkx as nx
import argparse
import sqlite3
import numpy as np
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple, Optional, Set, Any, Union
from dataclasses import dataclass, asdict, field
from enum import Enum
import logging
import hashlib
from collections import defaultdict, deque
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.collections import PatchCollection
import matplotlib.cm as cm
from sympy import symbols, Eq, solve, simplify, expand, factor, Derivative, Integral, pi, sin, cos, tan, sqrt
import itertools
from fractions import Fraction

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('theory_of_everything.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class SacredNumber(Enum):
    """Sacred numbers 1-7 with their geometric and symbolic meanings."""
    ONE = (1, "Unity", "Point", "God", "Beginning")
    TWO = (2, "Duality", "Line", "Polarity", "Relationship")
    THREE = (3, "Trinity", "Triangle", "Harmony", "Creation")
    FOUR = (4, "Foundation", "Square", "Earth", "Stability")
    FIVE = (5, "Life", "Pentagon", "Human", "Nature")
    SIX = (6, "Perfection", "Hexagon", "Creation", "Balance")
    SEVEN = (7, "Mystery", "Heptagon", "Spiritual", "Completion")

class SumerianBase60:
    """Sumerian sexagesimal (base-60) number system."""
    
    def __init__(self):
        self.base = 60
        self.symbols = {
            1: '𒐕', 2: '𒐖', 3: '𒐗', 4: '𒐘', 5: '𒐙',
            10: '𒑏', 20: '𒑚', 30: '𒑝', 40: '𒑠', 50: '𒑣'
        }
    
    def to_sexagesimal(self, decimal: float) -> str:
        """Convert decimal to sexagesimal."""
        whole = int(decimal)
        fractional = decimal - whole
        
        # Convert whole part
        sexa_parts = []
        temp = whole
        while temp > 0:
            sexa_parts.append(str(temp % 60))
            temp //= 60
        sexa_whole = ':'.join(reversed(sexa_parts)) if sexa_parts else '0'
        
        # Convert fractional part
        sexa_frac = []
        temp = fractional
        for _ in range(4):  # 4 places of precision
            temp *= 60
            sexa_frac.append(str(int(temp)))
            temp -= int(temp)
        sexa_fractional = ':'.join(sexa_frac) if any(int(x) for x in sexa_frac) else ''
        
        return f"{sexa_whole}{';' + sexa_fractional if sexa_fractional else ''}"
    
    def from_sexagesimal(self, sexa: str) -> float:
        """Convert sexagesimal to decimal."""
        if ';' in sexa:
            whole_part, frac_part = sexa.split(';')
        else:
            whole_part, frac_part = sexa, ''
        
        # Convert whole part
        whole_decimal = 0
        if whole_part:
            parts = whole_part.split(':')
            for i, part in enumerate(reversed(parts)):
                whole_decimal += int(part) * (60 ** i)
        
        # Convert fractional part
        frac_decimal = 0
        if frac_part:
            parts = frac_part.split(':')
            for i, part in enumerate(parts, 1):
                frac_decimal += int(part) / (60 ** i)
        
        return whole_decimal + frac_decimal

class SacredGeometry:
    """Sacred geometry patterns and their mathematical properties."""
    
    def __init__(self):
        self.golden_ratio = (1 + math.sqrt(5)) / 2
        self.silver_ratio = 1 + math.sqrt(2)
        self.plastic_ratio = ((9 + math.sqrt(69)) / 18) ** (1/3) + ((9 - math.sqrt(69)) / 18) ** (1/3)
    
    def generate_flower_of_life(self, n_circles: int = 7) -> List[Tuple[float, float, float]]:
        """Generate Flower of Life pattern."""
        circles = []
        center = (0, 0)
        radius = 1
        
        # Central circle
        circles.append((center[0], center[1], radius))
        
        # First ring (6 circles)
        for i in range(6):
            angle = i * math.pi / 3
            x = center[0] + 2 * radius * math.cos(angle)
            y = center[1] + 2 * radius * math.sin(angle)
            circles.append((x, y, radius))
        
        # Additional rings for larger patterns
        if n_circles > 7:
            for ring in range(2, (n_circles - 1) // 6 + 2):
                for i in range(6 * ring):
                    angle = i * math.pi / (3 * ring)
                    distance = 2 * radius * ring
                    x = center[0] + distance * math.cos(angle)
                    y = center[1] + distance * math.sin(angle)
                    circles.append((x, y, radius))
        
        return circles[:n_circles]
    
    def metatrons_cube_points(self) -> List[Tuple[float, float]]:
        """Generate points for Metatron's Cube (13 circles of Flower of Life)."""
        circles = self.generate_flower_of_life(19)  # 1 + 6 + 12
        points = []
        
        for x, y, r in circles:
            # Add points at 0, 60, 120, 180, 240, 300 degrees
            for angle in [0, 60, 120, 180, 240, 300]:
                rad = math.radians(angle)
                px = x + r * math.cos(rad)
                py = y + r * math.sin(rad)
                points.append((px, py))
        
        return points
    
    def platonic_solids_ratios(self) -> Dict[str, float]:
        """Return ratios for Platonic solids."""
        return {
            'tetrahedron': math.sqrt(2) / 12,
            'cube': 1,
            'octahedron': math.sqrt(2) / 3,
            'dodecahedron': (15 + 7 * math.sqrt(5)) / 4,
            'icosahedron': 5 * (3 + math.sqrt(5)) / 12
        }
    
    def fibonacci_spiral(self, n_points: int = 20) -> List[Tuple[float, float]]:
        """Generate Fibonacci spiral points."""
        points = []
        a, b = 0, 1
        
        for i in range(n_points):
            # Golden angle: 137.508 degrees
            angle = i * 137.508 * math.pi / 180
            radius = a + b
            
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            points.append((x, y))
            
            a, b = b, a + b
        
        return points

@dataclass
class EquationNode:
    """Enhanced equation node with sacred geometry connections."""
    id: str
    equation: str
    asciimath: str
    domain: str
    variables: List[str] = field(default_factory=list)
    constants: Dict[str, float] = field(default_factory=dict)
    sacred_number: Optional[int] = None
    geometry_pattern: Optional[str] = None
    base60_representation: Optional[str] = None
    pri_form: Optional[str] = None
    solved_for: Optional[str] = None
    dependencies: List[str] = field(default_factory=list)
    interconnections: Dict[str, List[str]] = field(default_factory=dict)  # domain -> connection_types
    confidence: float = 1.0
    source: str = ""
    timestamp: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()
        
        # Analyze for sacred geometry patterns
        self._analyze_sacred_patterns()
        
        # Convert constants to base-60
        self._convert_to_base60()
    
    def _analyze_sacred_patterns(self):
        """Analyze equation for sacred geometry patterns."""
        # Check for golden ratio
        if 'phi' in self.equation.lower() or 'φ' in self.equation:
            self.geometry_pattern = 'golden_ratio'
        
        # Check for pi
        if 'pi' in self.equation.lower() or 'π' in self.equation:
            self.geometry_pattern = 'circle'
        
        # Check for Fibonacci numbers
        fib_sequence = ['0', '1', '1', '2', '3', '5', '8', '13', '21', '34', '55', '89']
        for fib in fib_sequence:
            if f' {fib} ' in f' {self.equation} ':
                self.geometry_pattern = 'fibonacci'
                break
        
        # Determine sacred number (1-7)
        numbers = re.findall(r'\b([1-7])\b', self.equation)
        if numbers:
            self.sacred_number = int(numbers[0])
        
        # Check for geometric shapes
        shape_keywords = {
            'triangle': ['triangle', 'trig', 'sin', 'cos', 'tan'],
            'square': ['square', 'quad', '^2', 'squared'],
            'pentagon': ['pent', '5', 'five'],
            'hexagon': ['hex', '6', 'six', 'honeycomb'],
            'circle': ['circle', 'sphere', 'radial', 'radius'],
            'spiral': ['spiral', 'helix', 'vortex']
        }
        
        for shape, keywords in shape_keywords.items():
            for keyword in keywords:
                if keyword in self.equation.lower():
                    self.geometry_pattern = shape
                    break
    
    def _convert_to_base60(self):
        """Convert numeric constants to Sumerian base-60."""
        sumerian = SumerianBase60()
        
        for key, value in self.constants.items():
            if isinstance(value, (int, float)):
                self.constants[f"{key}_base60"] = sumerian.to_sexagesimal(value)

class PRIFramework:
    """
    Enhanced PRI Framework with sacred geometry and base-60 integration.
    Theorem of Persistent Reciprocal Identity implementation.
    """
    
    def __init__(self, conservation_constant: float = 1.0):
        self.S = conservation_constant  # Conservation constant
        self.anchor = 1.0  # Unitary anchor
        self.reciprocal_pairs = {}  # Maps x -> y where 1/x = y/1 = S
        self.sacred_geometry = SacredGeometry()
        self.sumerian = SumerianBase60()
        
        # Initialize with sacred ratios
        self._initialize_sacred_ratios()
    
    def _initialize_sacred_ratios(self):
        """Initialize PRI with sacred geometry ratios."""
        sacred_ratios = {
            'phi': self.sacred_geometry.golden_ratio,
            'pi': math.pi,
            'e': math.e,
            'sqrt2': math.sqrt(2),
            'sqrt3': math.sqrt(3),
            'sqrt5': math.sqrt(5)
        }
        
        for name, value in sacred_ratios.items():
            reciprocal = self.establish_pair(value)
            logger.info(f"PRI Pair: {name} = {value:.6f}, reciprocal = {reciprocal:.6f}")
    
    def establish_pair(self, x: float) -> float:
        """Establish reciprocal pair (x, y) satisfying PRI: 1/x = y/1 = S."""
        if x == 0:
            raise ValueError("x must be non-zero for reciprocal")
        
        y = self.S * x
        self.reciprocal_pairs[x] = y
        self.reciprocal_pairs[y] = x
        
        # Also store in base-60
        x_base60 = self.sumerian.to_sexagesimal(x)
        y_base60 = self.sumerian.to_sexagesimal(y)
        
        logger.debug(f"PRI Pair: {x} ({x_base60}) ↔ {y} ({y_base60}) with S={self.S}")
        
        return y
    
    def pri_transform(self, expression: str, preserve_structure: bool = True) -> str:
        """
        Transform expression to PRI form with explicit anchors.
        Maintains sacred geometry relationships.
        """
        try:
            # Convert to sympy
            expr = sympy.sympify(expression)
            
            # Apply PRI transformation
            transformed = self._apply_pri_recursive(expr, preserve_structure)
            
            # Convert back to string with sacred notation
            result = str(transformed)
            
            # Add sacred geometry annotations
            if preserve_structure:
                result = self._annotate_sacred_patterns(result)
            
            return result
            
        except Exception as e:
            logger.error(f"PRI transform error: {e}")
            return expression
    
    def _apply_pri_recursive(self, expr, preserve_structure: bool = True):
        """Recursively apply PRI transformation."""
        if expr.is_number:
            # Check if number has sacred geometry significance
            num = float(expr)
            if abs(num - self.sacred_geometry.golden_ratio) < 1e-10:
                return sympy.Symbol('φ')  # Golden ratio
            elif abs(num - math.pi) < 1e-10:
                return sympy.Symbol('π')  # Pi
            elif abs(num - math.e) < 1e-10:
                return sympy.Symbol('e')  # Euler's number
            
            # Apply PRI: n -> (1/n)*1
            if preserve_structure and num != 0:
                return sympy.Mul(sympy.Pow(sympy.Integer(1), sympy.Integer(1)), 
                               sympy.Pow(sympy.Integer(int(num) if num.is_integer() else num), 
                                       sympy.Integer(-1)))
            return expr
            
        elif expr.is_symbol:
            # Variable: x -> (1/x)*1
            if preserve_structure:
                return sympy.Mul(sympy.Pow(sympy.Integer(1), sympy.Integer(1)),
                               sympy.Pow(expr, sympy.Integer(-1)))
            return expr
            
        elif expr.is_mul:
            # Multiplication: maintain structure
            args = [self._apply_pri_recursive(arg, preserve_structure) for arg in expr.args]
            return sympy.Mul(*args)
            
        elif expr.is_add:
            # Addition: maintain structure
            args = [self._apply_pri_recursive(arg, preserve_structure) for arg in expr.args]
            return sympy.Add(*args)
            
        elif expr.is_pow:
            # Power: (a^b) -> maintain with PRI form
            base, exp = expr.as_base_exp()
            pri_base = self._apply_pri_recursive(base, preserve_structure)
            return sympy.Pow(pri_base, exp)
            
        elif expr.is_function:
            # Functions: maintain with arguments in PRI form
            args = [self._apply_pri_recursive(arg, preserve_structure) for arg in expr.args]
            return expr.func(*args)
        
        return expr
    
    def _annotate_sacred_patterns(self, expression: str) -> str:
        """Add sacred geometry annotations to expression."""
        annotations = []
        
        # Check for golden ratio
        if 'phi' in expression.lower() or 'φ' in expression:
            annotations.append('φ (Golden Ratio)')
        
        # Check for pi
        if 'pi' in expression.lower() or 'π' in expression:
            annotations.append('π (Circle Constant)')
        
        # Check for Fibonacci numbers
        fib_numbers = ['0', '1', '2', '3', '5', '8', '13', '21', '34', '55', '89']
        for fib in fib_numbers:
            if f' {fib} ' in f' {expression} ':
                annotations.append(f'F{len(fib_numbers)-fib_numbers.index(fib)} (Fibonacci)')
                break
        
        if annotations:
            return f"{expression} [{', '.join(annotations)}]"
        return expression
    
    def solve_with_pri(self, equation: str, target_var: str, 
                      known_vars: Dict[str, float] = None) -> Dict:
        """Solve equation using PRI framework with sacred geometry awareness."""
        if known_vars is None:
            known_vars = {}
        
        try:
            # Parse equation
            if '=' in equation:
                lhs, rhs = equation.split('=', 1)
                sympy_eq = Eq(sympy.sympify(lhs), sympy.sympify(rhs))
            else:
                sympy_eq = Eq(sympy.sympify(equation), 0)
            
            # Substitute known variables
            for var, value in known_vars.items():
                sympy_eq = sympy_eq.subs(sympy.Symbol(var), value)
            
                        # Solve for target variable
            target_sym = sympy.Symbol(target_var)
            solutions = solve(sympy_eq, target_sym)
            
            if not solutions:
                return {
                    'success': False,
                    'error': f'No solution found for {target_var}',
                    'method': 'pri_direct'
                }
            
            # Take first solution
            solution = solutions[0]
            
            # Apply PRI transformation
            pri_solution = self.pri_transform(str(solution), preserve_structure=True)
            
            # Convert to base-60
            try:
                numeric_solution = float(solution)
                base60_solution = self.sumerian.to_sexagesimal(numeric_solution)
            except:
                base60_solution = "Non-numeric"
            
            # Check for sacred geometry connections
            sacred_connections = self._find_sacred_connections(solution)
            
            return {
                'success': True,
                'variable': target_var,
                'solution': str(solution),
                'pri_solution': pri_solution,
                'base60': base60_solution,
                'sacred_connections': sacred_connections,
                'method': 'pri_direct',
                'confidence': 0.95
            }
            
        except Exception as e:
            logger.error(f"PRI solve error: {e}")
            return {
                'success': False,
                'error': str(e),
                'method': 'pri_direct'
            }
    
    def _find_sacred_connections(self, solution) -> List[str]:
        """Find sacred geometry connections in solution."""
        connections = []
        solution_str = str(solution)
        
        # Check for specific numbers
        numbers = re.findall(r'[-+]?\d*\.\d+|\d+', solution_str)
        for num in numbers:
            try:
                n = float(num)
                
                # Check for integers 1-7
                if n.is_integer() and 1 <= n <= 7:
                    connections.append(f"Sacred Number {int(n)}")
                
                # Check for golden ratio approximation
                if abs(n - self.sacred_geometry.golden_ratio) < 0.001:
                    connections.append("Golden Ratio φ")
                
                # Check for pi approximation
                if abs(n - math.pi) < 0.001:
                    connections.append("π (Pi)")
                
                # Check for e approximation
                if abs(n - math.e) < 0.001:
                    connections.append("e (Euler's Number)")
                
                # Check for square roots
                for root in [2, 3, 5]:
                    if abs(n - math.sqrt(root)) < 0.001:
                        connections.append(f"√{root}")
            
            except:
                pass
        
        return connections
    
    def fence_manifold(self, x: float) -> Dict:
        """
        Generate Fence Manifold for variable x.
        Shows both primary and reciprocal states with conservation constant S.
        """
        if x == 0:
            raise ValueError("x must be non-zero for Fence Manifold")
        
        y = self.establish_pair(x)
        
        return {
            'primary_state': {
                'numerator': 1,
                'denominator': x,
                'value': 1/x,
                'base60': self.sumerian.to_sexagesimal(1/x)
            },
            'reciprocal_state': {
                'numerator': y,
                'denominator': 1,
                'value': y,
                'base60': self.sumerian.to_sexagesimal(y)
            },
            'conservation_constant': {
                'S': self.S,
                'base60': self.sumerian.to_sexagesimal(self.S)
            },
            'equilibrium': f"1/{x} = {y}/1 = {self.S}",
            'sacred_check': self._check_sacred_number(x)
        }
    
    def _check_sacred_number(self, x: float) -> Dict:
        """Check if number has sacred geometry significance."""
        result = {'is_sacred': False, 'properties': []}
        
        if x.is_integer() and 1 <= x <= 7:
            result['is_sacred'] = True
            sacred = SacredNumber(int(x))
            result['properties'] = [f"{sacred.value[0]}: {sacred.value[1]} - {sacred.value[2]}"]
        
        # Check for golden ratio
        if abs(x - self.sacred_geometry.golden_ratio) < 1e-10:
            result['is_sacred'] = True
            result['properties'].append("Golden Ratio φ")
        
        # Check for pi
        if abs(x - math.pi) < 1e-10:
            result['is_sacred'] = True
            result['properties'].append("π (Circle Constant)")
        
        return result

class TheoryOfEverythingSolver:
    """
    Main Theory of Everything solver with PRI framework,
    sacred geometry, and Sumerian base-60 system.
    """
    
    def __init__(self, db_path: str = "theory_of_everything.db"):
        self.pri = PRIFramework()
        self.sacred_geometry = SacredGeometry()
        self.sumerian = SumerianBase60()
        self.knowledge_graph = nx.MultiDiGraph()
        self.equation_nodes = {}
        self.solution_paths = {}
        self.db_path = db_path
        self._init_database()
        
        # Initialize with fundamental equations
        self._initialize_fundamental_equations()
    
    def _init_database(self):
        """Initialize SQLite database for persistent storage."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create equations table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS equations (
                id TEXT PRIMARY KEY,
                equation TEXT NOT NULL,
                asciimath TEXT NOT NULL,
                domain TEXT NOT NULL,
                variables TEXT,
                constants TEXT,
                sacred_number INTEGER,
                geometry_pattern TEXT,
                base60_representation TEXT,
                pri_form TEXT,
                solved_for TEXT,
                confidence REAL,
                source TEXT,
                timestamp TEXT,
                metadata TEXT
            )
        ''')
        
        # Create solutions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS solutions (
                id TEXT PRIMARY KEY,
                equation_id TEXT,
                variable TEXT NOT NULL,
                value TEXT NOT NULL,
                pri_value TEXT,
                base60_value TEXT,
                sacred_connections TEXT,
                confidence REAL,
                method TEXT,
                dependencies TEXT,
                timestamp TEXT,
                FOREIGN KEY (equation_id) REFERENCES equations (id)
            )
        ''')
        
        # Create connections table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS connections (
                id TEXT PRIMARY KEY,
                from_equation TEXT,
                to_equation TEXT,
                connection_type TEXT,
                strength REAL,
                description TEXT,
                timestamp TEXT,
                FOREIGN KEY (from_equation) REFERENCES equations (id),
                FOREIGN KEY (to_equation) REFERENCES equations (id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def _initialize_fundamental_equations(self):
        """Initialize with fundamental equations from various domains."""
        fundamental_eqs = [
            # Mathematical
            ("Pythagorean Theorem", "a^2 + b^2 = c^2", "mathematical", ["a", "b", "c"]),
            ("Euler's Identity", "e^(iπ) + 1 = 0", "mathematical", ["e", "π", "i"]),
            ("Golden Ratio", "φ = (1 + sqrt(5))/2", "mathematical", ["φ"]),
            
            # Physics
            ("Newton's Second Law", "F = ma", "physics", ["F", "m", "a"]),
            ("Einstein's Mass-Energy", "E = mc^2", "physics", ["E", "m", "c"]),
            ("Schrodinger Equation", "iħ∂ψ/∂t = Hψ", "physics", ["i", "ħ", "ψ", "t", "H"]),
            
            # Chemistry
            ("Ideal Gas Law", "PV = nRT", "chemistry", ["P", "V", "n", "R", "T"]),
            ("Arrhenius Equation", "k = A e^(-Ea/RT)", "chemistry", ["k", "A", "Ea", "R", "T"]),
            
            # Biology
            ("Exponential Growth", "N = N0 e^(rt)", "biology", ["N", "N0", "r", "t"]),
            ("Michaelis-Menten", "v = Vmax[S]/(Km + [S])", "biology", ["v", "Vmax", "[S]", "Km"]),
            
            # Finance
            ("Compound Interest", "A = P(1 + r/n)^(nt)", "finance", ["A", "P", "r", "n", "t"]),
            ("Black-Scholes", "∂V/∂t + ½σ²S²∂²V/∂S² + rS∂V/∂S - rV = 0", "finance", ["V", "t", "σ", "S", "r"]),
        ]
        
        for name, eq, domain, vars in fundamental_eqs:
            eq_id = hashlib.md5(eq.encode()).hexdigest()[:16]
            node = EquationNode(
                id=eq_id,
                equation=eq,
                asciimath=eq,  # Simplified for example
                domain=domain,
                variables=vars,
                constants={},
                source="system_initialization"
            )
            self.add_equation(node)
    
    def add_equation(self, node: EquationNode):
        """Add equation to knowledge graph and database."""
        self.equation_nodes[node.id] = node
        self.knowledge_graph.add_node(
            node.id,
            equation=node.equation,
            domain=node.domain,
            sacred_number=node.sacred_number,
            geometry_pattern=node.geometry_pattern
        )
        
        # Save to database
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT OR REPLACE INTO equations 
            (id, equation, asciimath, domain, variables, constants, 
             sacred_number, geometry_pattern, base60_representation, 
             pri_form, solved_for, confidence, source, timestamp, metadata)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            node.id,
            node.equation,
            node.asciimath,
            node.domain,
            json.dumps(node.variables),
            json.dumps(node.constants),
            node.sacred_number,
            node.geometry_pattern,
            node.base60_representation,
            node.pri_form,
            node.solved_for,
            node.confidence,
            node.source,
            node.timestamp,
            json.dumps(node.metadata)
        ))
        
        conn.commit()
        conn.close()
        
        # Find connections to existing equations
        self._find_connections(node)
    
    def _find_connections(self, new_node: EquationNode):
        """Find connections between new equation and existing ones."""
        for eq_id, existing_node in self.equation_nodes.items():
            if eq_id == new_node.id:
                continue
            
            connection_types = []
            
            # Check shared variables
            shared_vars = set(new_node.variables) & set(existing_node.variables)
            if shared_vars:
                connection_types.append(f"shared_variables:{','.join(shared_vars)}")
            
            # Check same sacred number
            if (new_node.sacred_number and existing_node.sacred_number and 
                new_node.sacred_number == existing_node.sacred_number):
                connection_types.append(f"sacred_number:{new_node.sacred_number}")
            
            # Check same geometry pattern
            if (new_node.geometry_pattern and existing_node.geometry_pattern and
                new_node.geometry_pattern == existing_node.geometry_pattern):
                connection_types.append(f"geometry:{new_node.geometry_pattern}")
            
            # Check mathematical similarity
            similarity = self._calculate_similarity(new_node.equation, existing_node.equation)
            if similarity > 0.3:
                connection_types.append(f"mathematical_similarity:{similarity:.2f}")
            
            # Add connections to graph
            for conn_type in connection_types:
                self.knowledge_graph.add_edge(
                    new_node.id, existing_node.id,
                    connection_type=conn_type,
                    weight=similarity
                )
                
                # Save to database
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
                conn_id = hashlib.md5(f"{new_node.id}{existing_node.id}{conn_type}".encode()).hexdigest()[:16]
                
                cursor.execute('''
                    INSERT OR REPLACE INTO connections 
                    (id, from_equation, to_equation, connection_type, strength, description, timestamp)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    conn_id,
                    new_node.id,
                    existing_node.id,
                    conn_type,
                    similarity,
                    f"Connection between {new_node.domain} and {existing_node.domain}",
                    datetime.now().isoformat()
                ))
                
                conn.commit()
                conn.close()
    
    def _calculate_similarity(self, eq1: str, eq2: str) -> float:
        """Calculate similarity between two equations."""
        # Simple token-based similarity
        tokens1 = set(re.findall(r'[a-zA-Zα-ωΑ-Ω_]+', eq1))
        tokens2 = set(re.findall(r'[a-zA-Zα-ωΑ-Ω_]+', eq2))
        
        if not tokens1 or not tokens2:
            return 0.0
        
        intersection = tokens1.intersection(tokens2)
        union = tokens1.union(tokens2)
        
        return len(intersection) / len(union)
    
    def solve_system(self, target_var: str, known_vars: Dict[str, float] = None, 
                    max_depth: int = 5) -> Dict:
        """
        Solve for target variable using interconnected equations.
        Uses PRI framework and sacred geometry insights.
        """
        if known_vars is None:
            known_vars = {}
        
        logger.info(f"Solving for {target_var} with known: {known_vars}")
        
        # Track solution path
        solution_path = []
        visited_nodes = set()
        
        def dfs_search(current_var: str, path: List[Tuple[str, str]], depth: int = 0):
            """Depth-first search through equation network."""
            if depth > max_depth:
                return None
            
            if current_var in known_vars:
                return path
            
            # Find equations containing current_var
            candidate_eqs = []
            for eq_id, node in self.equation_nodes.items():
                if current_var in node.variables and eq_id not in visited_nodes:
                    # Count how many variables we already know
                    known_in_eq = sum(1 for v in node.variables if v in known_vars)
                    candidate_eqs.append((eq_id, node, known_in_eq))
            
            # Sort by number of known variables (prefer equations with more knowns)
            candidate_eqs.sort(key=lambda x: x[2], reverse=True)
            
            for eq_id, node, _ in candidate_eqs:
                visited_nodes.add(eq_id)
                
                # Try to solve this equation
                solution = self._solve_single_equation(node, current_var, known_vars)
                
                if solution['success']:
                    # Add to known variables
                    try:
                        value = float(solution['solution'])
                        known_vars[current_var] = value
                        solution_path.append({
                            'equation_id': eq_id,
                            'equation': node.equation,
                            'variable': current_var,
                            'solution': solution['solution'],
                            'pri_form': solution.get('pri_solution'),
                            'base60': solution.get('base60'),
                            'sacred_connections': solution.get('sacred_connections', []),
                            'method': solution['method']
                        })
                        
                        # Check if we can now solve for other variables
                        for other_var in node.variables:
                            if other_var != current_var and other_var not in known_vars:
                                result = dfs_search(other_var, path + [(eq_id, current_var)], depth + 1)
                                if result:
                                    return result
                        
                        return path + [(eq_id, current_var)]
                    
                    except (ValueError, TypeError):
                        continue
            
            return None
        
        # Start search
        path = dfs_search(target_var, [])
        
        if path:
            return {
                'success': True,
                'target_variable': target_var,
                'value': known_vars.get(target_var),
                'solution_path': solution_path,
                'known_variables': known_vars,
                'method': 'graph_search_with_pri'
            }
        else:
            # Try direct PRI solve
            for eq_id, node in self.equation_nodes.items():
                if target_var in node.variables:
                    solution = self._solve_single_equation(node, target_var, known_vars)
                    if solution['success']:
                        return {
                            'success': True,
                            'target_variable': target_var,
                            'value': solution.get('solution'),
                            'solution_path': [{
                                'equation_id': eq_id,
                                'equation': node.equation,
                                'variable': target_var,
                                'solution': solution['solution'],
                                'pri_form': solution.get('pri_solution'),
                                'base60': solution.get('base60'),
                                'sacred_connections': solution.get('sacred_connections', []),
                                'method': solution['method']
                            }],
                            'known_variables': known_vars,
                            'method': 'direct_pri'
                        }
            
            return {
                'success': False,
                'error': f'Could not solve for {target_var}',
                'known_variables': known_vars
            }
    
    def _solve_single_equation(self, node: EquationNode, target_var: str, 
                              known_vars: Dict[str, float]) -> Dict:
        """Solve a single equation for target variable."""
        # Try direct solve first
        result = self.pri.solve_with_pri(node.equation, target_var, known_vars)
        
        if result['success']:
            return result
        
        # Try rearranging equation
        return self._rearrange_equation(node, target_var, known_vars)
    
        def _rearrange_equation(self, node: EquationNode, target_var: str,
                           known_vars: Dict[str, float]) -> Dict:
        """Attempt to rearrange equation to solve for target variable."""
        try:
            # Convert equation to sympy
            eq_str = node.equation
            
            # Handle different equation formats
            if '=' in eq_str:
                lhs, rhs = eq_str.split('=', 1)
                expr = sympy.sympify(f"{lhs} - ({rhs})")
                sympy_eq = Eq(sympy.sympify(lhs), sympy.sympify(rhs))
            else:
                expr = sympy.sympify(eq_str)
                sympy_eq = Eq(expr, 0)
            
            # Get all variables
            all_vars = list(expr.free_symbols)
            var_names = [str(v) for v in all_vars]
            
            if target_var not in var_names:
                return {'success': False, 'error': f'Variable {target_var} not in equation'}
            
            # Substitute known values
            for var, value in known_vars.items():
                if var in var_names:
                    sympy_eq = sympy_eq.subs(sympy.Symbol(var), value)
            
            # Try to solve algebraically
            target_sym = sympy.Symbol(target_var)
            solutions = solve(sympy_eq, target_sym)
            
            if solutions:
                solution = solutions[0]
                
                # Apply PRI transformation
                pri_solution = self.pri.pri_transform(str(solution), preserve_structure=True)
                
                # Check for sacred geometry connections
                sacred_connections = self.pri._find_sacred_connections(solution)
                
                # Convert to base-60 if numeric
                try:
                    numeric_val = float(solution)
                    base60_val = self.sumerian.to_sexagesimal(numeric_val)
                except:
                    base60_val = "Symbolic"
                
                return {
                    'success': True,
                    'solution': str(solution),
                    'pri_solution': pri_solution,
                    'base60': base60_val,
                    'sacred_connections': sacred_connections,
                    'method': 'algebraic_rearrangement',
                    'confidence': 0.85
                }
            
            # Try numerical approximation if we have enough knowns
            unknown_vars = [v for v in var_names if v not in known_vars and v != target_var]
            
            if len(unknown_vars) == 0:
                # All other variables known, solve numerically
                # Create function f(target) = 0
                f = sympy.lambdify(target_sym, sympy_eq.lhs - sympy_eq.rhs, 'numpy')
                
                # Use binary search for root
                left, right = -1000, 1000
                f_left, f_right = f(left), f(right)
                
                if f_left * f_right > 0:
                    return {'success': False, 'error': 'No root found in range'}
                
                for _ in range(50):  # Binary search iterations
                    mid = (left + right) / 2
                    f_mid = f(mid)
                    
                    if abs(f_mid) < 1e-10:
                        solution = mid
                        break
                    elif f_left * f_mid <= 0:
                        right = mid
                        f_right = f_mid
                    else:
                        left = mid
                        f_left = f_mid
                else:
                    solution = (left + right) / 2
                
                # Apply PRI transformation
                pri_solution = self.pri.pri_transform(str(solution), preserve_structure=True)
                
                return {
                    'success': True,
                    'solution': str(solution),
                    'pri_solution': pri_solution,
                    'base60': self.sumerian.to_sexagesimal(solution),
                    'sacred_connections': self.pri._find_sacred_connections(solution),
                    'method': 'numerical_approximation',
                    'confidence': 0.75
                }
            
            return {'success': False, 'error': 'Insufficient known variables'}
            
        except Exception as e:
            logger.error(f"Equation rearrangement error: {e}")
            return {'success': False, 'error': str(e)}
    
    def find_interconnections(self, eq_id1: str, eq_id2: str, 
                            max_paths: int = 10) -> List[List[str]]:
        """Find all connection paths between two equations."""
        if eq_id1 not in self.knowledge_graph or eq_id2 not in self.knowledge_graph:
            return []
        
        try:
            paths = list(nx.all_simple_paths(self.knowledge_graph, eq_id1, eq_id2, cutoff=5))
            
            # Sort by path length and connection strength
            scored_paths = []
            for path in paths[:max_paths]:
                score = 0
                for i in range(len(path) - 1):
                    edge_data = self.knowledge_graph.get_edge_data(path[i], path[i+1])
                    if edge_data:
                        # Sum weights from all connections between nodes
                        for key in edge_data:
                            score += edge_data[key].get('weight', 0)
                
                # Apply sacred geometry bonus
                for node_id in path:
                    node = self.equation_nodes.get(node_id)
                    if node and node.sacred_number:
                        score += 0.1 * node.sacred_number
                
                scored_paths.append((score, path))
            
            scored_paths.sort(key=lambda x: x[0], reverse=True)
            return [path for _, path in scored_paths]
            
        except:
            return []
    
    def generate_sacred_geometry_visualization(self, output_path: str = "sacred_geometry.png"):
        """Create visualization showing equations in sacred geometry patterns."""
        plt.figure(figsize=(20, 20))
        
        # Create Flower of Life background
        circles = self.sacred_geometry.generate_flower_of_life(19)
        
        # Plot circles
        for x, y, r in circles:
            circle = plt.Circle((x, y), r, fill=False, color='lightblue', alpha=0.3, linewidth=0.5)
            plt.gca().add_patch(circle)
        
        # Position equations based on domain and sacred number
        positions = {}
        domain_angles = {
            'mathematical': 0,
            'physics': 60,
            'chemistry': 120,
            'biology': 180,
            'finance': 240,
            'economics': 300,
            'computer_science': 30,
            'engineering': 90,
            'interdisciplinary': 150,
            'unknown': 210
        }
        
        for eq_id, node in self.equation_nodes.items():
            angle = domain_angles.get(node.domain, 0)
            
            # Use sacred number for radius
            if node.sacred_number:
                radius = node.sacred_number * 0.8
            else:
                radius = 3.0
            
            # Add golden ratio spiral offset for sacred numbers
            if node.sacred_number in [1, 2, 3, 5, 8, 13]:
                # Fibonacci positions
                fib_idx = [1, 2, 3, 5, 8, 13].index(node.sacred_number)
                spiral_angle = fib_idx * 137.508 * math.pi / 180
                x = radius * math.cos(spiral_angle)
                y = radius * math.sin(spiral_angle)
            else:
                # Regular circular position
                rad_angle = math.radians(angle)
                x = radius * math.cos(rad_angle)
                y = radius * math.sin(rad_angle)
            
            positions[eq_id] = (x, y)
            
            # Plot node
            color_map = {
                1: 'red', 2: 'orange', 3: 'yellow', 
                4: 'green', 5: 'blue', 6: 'indigo', 7: 'violet'
            }
            
            color = color_map.get(node.sacred_number, 'gray')
            plt.scatter(x, y, s=500, c=color, alpha=0.7, edgecolors='black')
            
            # Add equation label (abbreviated)
            label = node.equation[:20] + '...' if len(node.equation) > 20 else node.equation
            plt.text(x, y + 0.2, label, fontsize=6, ha='center', 
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.7))
        
        # Draw connections
        for edge in self.knowledge_graph.edges():
            if edge[0] in positions and edge[1] in positions:
                x1, y1 = positions[edge[0]]
                x2, y2 = positions[edge[1]]
                
                # Get connection type for styling
                edge_data = self.knowledge_graph.get_edge_data(edge[0], edge[1])
                if edge_data:
                    conn_type = list(edge_data.values())[0].get('connection_type', '')
                    
                    if 'sacred' in conn_type:
                        plt.plot([x1, x2], [y1, y2], 'gold', alpha=0.3, linewidth=2)
                    elif 'golden' in conn_type:
                        plt.plot([x1, x2], [y1, y2], 'orange', alpha=0.3, linewidth=1.5)
                    else:
                        plt.plot([x1, x2], [y1, y2], 'gray', alpha=0.2, linewidth=0.5)
        
        plt.title("Theory of Everything: Sacred Geometry Network", fontsize=16)
        plt.axis('equal')
        plt.axis('off')
        
        # Add legend
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='red', label='Sacred 1: Unity'),
            Patch(facecolor='orange', label='Sacred 2: Duality'),
            Patch(facecolor='yellow', label='Sacred 3: Trinity'),
            Patch(facecolor='green', label='Sacred 4: Foundation'),
            Patch(facecolor='blue', label='Sacred 5: Life'),
            Patch(facecolor='indigo', label='Sacred 6: Perfection'),
            Patch(facecolor='violet', label='Sacred 7: Mystery'),
            Patch(facecolor='gray', label='Other Numbers')
        ]
        
        plt.legend(handles=legend_elements, loc='upper left', fontsize=8)
        
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        logger.info(f"Sacred geometry visualization saved to {output_path}")
    
    def export_knowledge_tree(self, output_path: str = "knowledge_tree.json"):
        """Export entire knowledge graph with PRI transformations."""
        tree = {
            'metadata': {
                'export_date': datetime.now().isoformat(),
                'total_equations': len(self.equation_nodes),
                'pri_framework': {
                    'conservation_constant': self.pri.S,
                    'unitary_anchor': self.pri.anchor
                },
                'sacred_geometry': {
                    'golden_ratio': self.sacred_geometry.golden_ratio,
                    'silver_ratio': self.sacred_geometry.silver_ratio
                }
            },
            'equations': [],
            'connections': []
        }
        
        # Export equations
        for eq_id, node in self.equation_nodes.items():
            eq_data = asdict(node)
            
            # Add PRI form if not already present
            if not eq_data['pri_form']:
                eq_data['pri_form'] = self.pri.pri_transform(node.equation)
            
            # Add base-60 representations for constants
            base60_constants = {}
            for key, value in node.constants.items():
                if isinstance(value, (int, float)):
                    base60_constants[f"{key}_base60"] = self.sumerian.to_sexagesimal(value)
            
            eq_data['base60_constants'] = base60_constants
            tree['equations'].append(eq_data)
        
        # Export connections
        for edge in self.knowledge_graph.edges(data=True):
            conn_data = {
                'from': edge[0],
                'to': edge[1],
                'type': edge[2].get('connection_type', ''),
                'weight': edge[2].get('weight', 0),
                'description': f"Connection between equations"
            }
            tree['connections'].append(conn_data)
        
        # Save to file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(tree, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Knowledge tree exported to {output_path}")
        return tree
    
    def import_equations_from_file(self, file_path: str, file_type: str = None):
        """Import equations from various file formats."""
        from equation_extractor import EquationExtractor  # Import from previous code
        
        extractor = EquationExtractor()
        
        if file_type == 'auto' or file_type is None:
            # Auto-detect based on extension
            ext = Path(file_path).suffix.lower()
            if ext in ['.pdf', '.txt', '.docx', '.doc', '.odt', '.odf']:
                equations = extractor.extract_from_file(file_path)
            elif ext in ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp']:
                equations = extractor.extract_from_image(file_path)
            else:
                logger.error(f"Unsupported file type: {ext}")
                return []
        else:
            # Use specified extractor method
            if file_type == 'pdf':
                equations = extractor.extract_from_pdf(file_path)
            elif file_type == 'image':
                equations = extractor.extract_from_image(file_path)
            elif file_type == 'text':
                equations = extractor.extract_from_txt(file_path)
            elif file_type == 'docx':
                equations = extractor.extract_from_docx(file_path)
            else:
                logger.error(f"Unsupported file type: {file_type}")
                return []
        
        # Convert to EquationNode format and add to solver
        added_count = 0
        for eq in equations:
            # Extract variables from ASCIIMath
            variables = self._extract_variables_from_asciimath(eq.asciimath)
            
            # Create EquationNode
            node = EquationNode(
                id=eq.id,
                equation=eq.content,
                asciimath=eq.asciimath,
                domain=eq.equation_type.value,
                variables=variables,
                constants={},
                source=eq.source_file,
                confidence=eq.confidence,
                metadata=eq.metadata
            )
            
            self.add_equation(node)
            added_count += 1
        
        logger.info(f"Imported {added_count} equations from {file_path}")
        return added_count
    
    def _extract_variables_from_asciimath(self, asciimath: str) -> List[str]:
        """Extract variable names from ASCIIMath expression."""
        # Remove numbers, constants, and common functions
        expr = re.sub(r'\d+\.?\d*', '', asciimath)  # Remove numbers
        expr = re.sub(r'[+\-*/^()\[\]{}]', ' ', expr)  # Replace operators with spaces
        expr = re.sub(r'\b(sin|cos|tan|log|ln|exp|sqrt|sum|int|lim)\b', '', expr, flags=re.IGNORECASE)
        
        # Find variable-like tokens (single letters or words)
        tokens = re.findall(r'\b[a-zA-Zα-ωΑ-Ω_][a-zA-Zα-ωΑ-Ω0-9_]*\b', expr)
        
        # Filter out common constants
        constants = ['pi', 'π', 'e', 'phi', 'φ', 'gamma', 'γ', 'alpha', 'α', 'beta', 'β']
        variables = [t for t in tokens if t.lower() not in constants and len(t) <= 3]
        
        return list(set(variables))  # Remove duplicates

class InteractiveTheoryCLI:
    """Interactive command-line interface for Theory of Everything solver."""
    
    def __init__(self):
        self.solver = TheoryOfEverythingSolver()
        self.running = True
    
    def run(self):
        """Run the interactive CLI."""
        print("=" * 70)
        print("THEORY OF EVERYTHING EQUATION SOLVER")
        print("With PRI Framework & Sacred Geometry")
        print("=" * 70)
        
        while self.running:
            print("\n" + "=" * 50)
            print("MAIN MENU")
            print("=" * 50)
            print("1. Import equations from file")
            print("2. Enter equation manually")
            print("3. Solve for variable")
            print("4. Show equation network")
            print("5. Generate sacred geometry visualization")
            print("6. Explore PRI framework")
            print("7. Show database statistics")
            print("8. Export knowledge tree")
            print("9. Find connections between equations")
            print("0. Exit")
            print("-" * 50)
            
            choice = input("Enter your choice (0-9): ").strip()
            
            if choice == '1':
                self.import_equations()
            elif choice == '2':
                self.enter_equation_manual()
            elif choice == '3':
                self.solve_for_variable()
            elif choice == '4':
                self.show_network()
            elif choice == '5':
                self.generate_visualization()
            elif choice == '6':
                self.explore_pri()
            elif choice == '7':
                self.show_statistics()
            elif choice == '8':
                self.export_tree()
            elif choice == '9':
                self.find_connections()
            elif choice == '0':
                print("Exiting...")
                self.running = False
            else:
                print("Invalid choice. Please try again.")
    
    def import_equations(self):
        """Import equations from file."""
        print("\n" + "-" * 50)
        print("IMPORT EQUATIONS")
        print("-" * 50)
        
        file_path = input("Enter file path: ").strip()
        
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return
        
        print("\nFile types:")
        print("1. PDF")
        print("2. Image (JPG, PNG, GIF, TIFF, BMP)")
        print("3. Text file")
        print("4. Word document (DOCX)")
        print("5. Auto-detect")
        
        type_choice = input("Select file type (1-5): ").strip()
        
        file_types = {
            '1': 'pdf',
            '2': 'image',
            '3': 'text',
            '4': 'docx',
            '5': 'auto'
        }
        
        file_type = file_types.get(type_choice, 'auto')
        
        try:
            count = self.solver.import_equations_from_file(file_path, file_type)
            print(f"\nSuccessfully imported {count} equations")
            
            # Show summary
            domains = {}
            for node in self.solver.equation_nodes.values():
                domains[node.domain] = domains.get(node.domain, 0) + 1
            
            print("\nImported by domain:")
            for domain, count in domains.items():
                print(f"  {domain}: {count}")
                
        except Exception as e:
            print(f"Error importing equations: {e}")
    
    def enter_equation_manual(self):
        """Enter equation manually."""
        print("\n" + "-" * 50)
        print("ENTER EQUATION MANUALLY")
        print("-" * 50)
        
        equation = input("Enter equation (e.g., F = ma, E = mc^2): ").strip()
        if not equation:
            print("No equation entered.")
            return
        
        asciimath = input("Enter ASCIIMath representation (press Enter to use same as equation): ").strip()
        if not asciimath:
            asciimath = equation
        
        print("\nSelect domain:")
        for i, domain in enumerate(EquationDomain, 1):
            print(f"{i}. {domain.value}")
        
        domain_choice = input("Select domain (1-10): ").strip()
        try:
            domain_idx = int(domain_choice) - 1
            if 0 <= domain_idx < len(EquationDomain):
                domain = list(EquationDomain)[domain_idx].value
            else:
                domain = "unknown"
        except:
            domain = "unknown"
        
        # Extract variables
        variables = self.solver._extract_variables_from_asciimath(asciimath)
        
        # Create equation node
        eq_id = hashlib.md5(equation.encode()).hexdigest()[:16]
        node = EquationNode(
            id=eq_id,
            equation=equation,
            asciimath=asciimath,
            domain=domain,
            variables=variables,
            source="manual_input"
        )
        
        self.solver.add_equation(node)
        
        print(f"\nAdded equation: {equation}")
        print(f"Variables detected: {', '.join(variables)}")
        print(f"Domain: {domain}")
        
        # Show PRI form
        pri_form = self.solver.pri.pri_transform(equation)
        print(f"PRI form: {pri_form}")
    
    def solve_for_variable(self):
        """Solve for a specific variable."""
        print("\n" + "-" * 50)
        print("SOLVE FOR VARIABLE")
        print("-" * 50)
        
        # Show available equations
        if not self.solver.equation_nodes:
            print("No equations in database. Please import or enter equations first.")
            return
        
        print("\nAvailable equations:")
        for i, (eq_id, node) in enumerate(list(self.solver.equation_nodes.items())[:10], 1):
            print(f"{i}. {node.equation} ({node.domain})")
        
        if len(self.solver.equation_nodes) > 10:
            print(f"... and {len(self.solver.equation_nodes) - 10} more")
        
        target_var = input("\nEnter variable to solve for (e.g., x, F, E): ").strip()
        if not target_var:
            print("No variable specified.")
            return
        
        # Get known variables
        known_vars = {}
        print("\nEnter known variables (leave blank when done):")
        while True:
            var_name = input("Variable name: ").strip()
            if not var_name:
                break
            
            var_value = input(f"Value for {var_name}: ").strip()
            try:
                value = float(var_value)
                known_vars[var_name] = value
                print(f"  Added {var_name} = {value}")
            except ValueError:
                print(f"  Invalid number: {var_value}")
        
        print(f"\nSolving for {target_var} with known variables: {known_vars}")
        
        # Solve using theory of everything solver
        result = self.solver.solve_system(target_var, known_vars)
        
        if result['success']:
            print(f"\n✓ SUCCESS: {target_var} = {result['value']}")
            
            if 'solution_path' in result:
                print("\nSolution path:")
                for step in result['solution_path']:
                    print(f"  • {step['equation']}")
                    print(f"    → {step['variable']} = {step['solution']}")
                    if step.get('pri_form'):
                        print(f"    PRI form: {step['pri_form']}")
                    if step.get('base60'):
                        print(f"    Base-60: {step['base60']}")
                    if step.get('sacred_connections'):
                        print(f"    Sacred connections: {', '.join(step['sacred_connections'])}")
                    print()
            
            # Show in Sumerian base-60
            try:
                value_num = float(result['value'])
                base60 = self.solver.sumerian.to_sexagesimal(value_num)
                print(f"Sumerian base-60: {base60}")
            except:
                pass
            
            # Show Fence Manifold if applicable
            try:
                fence = self.solver.pri.fence_manifold(float(result['value']))
                print(f"\nFence Manifold:")
                print(f"  Primary: 1/{result['value']} = {fence['primary_state']['value']:.6f}")
                print(f"  Reciprocal: {fence['reciprocal_state']['value']:.6f}/1 = {fence['reciprocal_state']['value']:.6f}")
                print(f"  Conservation constant S = {fence['conservation_constant']['S']}")
                
                if fence['sacred_check']['is_sacred']:
                    print(f"  Sacred properties: {', '.join(fence['sacred_check']['properties'])}")
            except:
                pass
            
        else:
            print(f"\n✗ FAILED: {result.get('error', 'Unknown error')}")
            
            # Suggest alternative approaches
            print("\nSuggestions:")
            print("1. Add more known variables")
            print("2. Check variable names match equations")
            print("3. Try solving for a different variable first")
            print("4. Add more equations to the database")
    
    def show_network(self):
        """Display the equation network."""
        print("\n" + "-" * 50)
        print("EQUATION NETWORK")
        print("-" * 50)
        
        if not self.solver.equation_nodes:
            print("No equations in network.")
            return
        
        print(f"Total equations: {len(self.solver.equation_nodes)}")
        print(f"Total connections: {self.solver.knowledge_graph.number_of_edges()}")
        
        # Show by domain
        domains = {}
        for node in self.solver.equation_nodes.values():
            domains[node.domain] = domains.get(node.domain, 0) + 1
        
        print("\nEquations by domain:")
        for domain, count in sorted(domains.items()):
            print(f"  {domain}: {count}")
        
        # Show sacred numbers
        sacred_counts = {}
        for node in self.solver.equation_nodes.values():
            if node.sacred_number:
                sacred_counts[node.sacred_number] = sacred_counts.get(node.sacred_number, 0) + 1
        
        if sacred_counts:
            print("\nEquations with sacred numbers:")
            for num in sorted(sacred_counts.keys()):
                sacred = SacredNumber(num)
                print(f"  {num} ({sacred.value[1]}): {sacred_counts[num]}")
        
        # Show most connected equations
        print("\nMost interconnected equations:")
        centrality = nx.degree_centrality(self.solver.knowledge_graph)
        top_nodes = sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:5]
        
        for eq_id, score in top_nodes:
            node = self.solver.equation_nodes[eq_id]
            print(f"  {node.equation[:40]}... (Connections: {self.solver.knowledge_graph.degree(eq_id)})")
    
    def generate_visualization(self):
        """Generate sacred geometry visualization."""
        print("\n" + "-" * 50)
        print("GENERATE SACRED GEOMETRY VISUALIZATION")
        print("-" * 50)
        
        if not self.solver.equation_nodes:
            print("No equations to visualize.")
            return
        
        output_path = input("Enter output file name (default: sacred_geometry.png): ").strip()
        if not output_path:
            output_path = "sacred_geometry.png"
        
        print("Generating visualization...")
        self.solver.generate_sacred_geometry_visualization(output_path)
        print(f"Visualization saved to {output_path}")
        
        # Also generate regular graph
        output_path2 = output_path.replace('.png', '_graph.png')
        self._generate_graph_visualization(output_path2)
        print(f"Network graph saved to {output_path2}")
    
    def _generate_graph_visualization(self, output_path: str):
        """Generate regular network graph visualization."""
        plt.figure(figsize=(15, 15))
        
        # Use spring layout
        pos = nx.spring_layout(self.solver.knowledge_graph, k=2, iterations=50)
        
        # Color by domain
        domain_colors = {
            'mathematical': 'lightblue',
            'physics': 'lightcoral',
            'chemistry': 'lightgreen',
            'biology': 'lightyellow',
            'finance': 'lightpink',
            'economics': 'lightgray',
            'computer_science': 'lightcyan',
            'engineering': 'wheat',
            'interdisciplinary': 'violet',
            'unknown': 'white'
        }
        
        node_colors = []
        for node in self.solver.knowledge_graph.nodes():
            domain = self.solver.equation_nodes[node].domain
            node_colors.append(domain_colors.get(domain, 'white'))
        
        # Draw
        nx.draw_networkx_nodes(self.solver.knowledge_graph, pos, 
                              node_color=node_colors, node_size=300, alpha=0.8)
        nx.draw_networkx_edges(self.solver.knowledge_graph, pos, alpha=0.3, width=1)
        
        # Add labels for important nodes
        labels = {}
        for node in self.solver.knowledge_graph.nodes():
            if self.solver.knowledge_graph.degree(node) > 2:  # Only label highly connected nodes
                eq = self.solver.equation_nodes[node].equation
                labels[node] = eq[:10] + '...' if len(eq) > 10 else eq
        
        nx.draw_networkx_labels(self.solver.knowledge_graph, pos, labels, font_size=8)
        
        plt.title("Theory of Everything Equation Network", fontsize=16)
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
    
    def explore_pri(self):
        """Explore the PRI framework."""
        print("\n" + "-" * 50)
        print("PERSISTENT RECIPROCAL IDENTITY FRAMEWORK")
        print("-" * 50)
        
        print("\nPRI Theorem: For any non-zero real variable x,")
        print("there exists a co-equal reciprocal variable y,")
        print("such that both 1/x and y/1 are conserved under constant S.")
        print(f"\nCurrent conservation constant S = {self.solver.pri.S}")
        print(f"Unitary anchor = {self.solver.pri.anchor}")
        
        while True:
            print("\nPRI Operations:")
            print("1. Create reciprocal pair")
            print("2. Transform equation to PRI form")
            print("3. Generate Fence Manifold")
            print("4. Show all reciprocal pairs")
            print("5. Back to main menu")
            
            choice = input("\nSelect operation (1-5): ").strip()
            
            if choice == '1':
                try:
                    x = float(input("Enter value for x: "))
                    y = self.solver.pri.establish_pair(x)
                    print(f"Reciprocal pair created:")
                    print(f"  x = {x}")
                    print(f"  y = {y}")
                    print(f"  1/{x} = {y}/1 = {self.solver.pri.S}")
                    print(f"  Base-60: x = {self.solver.sumerian.to_sexagesimal(x)}")
                    print(f"            y = {self.solver.sumerian.to_sexagesimal(y)}")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == '2':
                equation = input("Enter equation to transform: ")
                pri_form = self.solver.pri.pri_transform(equation)
                print(f"\nOriginal: {equation}")
                print(f"PRI form: {pri_form}")
            
            elif choice == '3':
                try:
                    x = float(input("Enter value for x: "))
                    fence = self.solver.pri.fence_manifold(x)
                    
                    print(f"\nFence Manifold for x = {x}:")
                    print(f"Primary State:   1/{x} = {fence['primary_state']['value']:.6f}")
                    print(f"Reciprocal State: {fence['reciprocal_state']['value']:.6f}/1 = {fence['reciprocal_state']['value']:.6f}")
                    print(f"Conservation Constant S = {fence['conservation_constant']['S']}")
                    print(f"\nBase-60 representations:")
                    print(f"  1/{x} = {fence['primary_state']['base60']}")
                    print(f"  {fence['reciprocal_state']['value']:.6f}/1 = {fence['reciprocal_state']['base60']}")
                    print(f"  S = {fence['conservation_constant']['base60']}")
                    
                    if fence['sacred_check']['is_sacred']:
                        print(f"\nSacred properties detected:")
                        for prop in fence['sacred_check']['properties']:
                            print(f"  • {prop}")
                    
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == '4':
                print("\nReciprocal pairs:")
                for x, y in self.solver.pri.reciprocal_pairs.items():
                    if x < y:  # Show each pair only once
                        print(f"  {x:.6f} ↔ {y:.6f}")
                
                if not self.solver.pri.reciprocal_pairs:
                    print("  No reciprocal pairs created yet.")
            
            elif choice == '5':
                break
    
    def show_statistics(self):
        """Show database statistics."""
        print("\n" + "-" * 50)
        print("DATABASE STATISTICS")
        print("-" * 50)
        
        # Connect to database
        conn = sqlite3.connect(self.solver.db_path)
        cursor = conn.cursor()
        
        # Count equations
        cursor.execute("SELECT COUNT(*) FROM equations")
        total_eq = cursor.fetchone()[0]
        
        print(f"Total equations: {total_eq}")
        
        # Count by domain
        cursor.execute("SELECT domain, COUNT(*) FROM equations GROUP BY domain ORDER BY COUNT(*) DESC")
        print("\nEquations by domain:")
        for domain, count in cursor.fetchall():
            print(f"  {domain}: {count}")
        
        # Count by sacred number
        cursor.execute("SELECT sacred_number, COUNT(*) FROM equations WHERE sacred_number IS NOT NULL GROUP BY sacred_number ORDER BY sacred_number")
        print("\nEquations by sacred number:")
        for num, count in cursor.fetchall():
            sacred = SacredNumber(num)
            print(f"  {num} ({sacred.value[1]}): {count}")
        
        # Most common variables
        all_vars = []
        for node in self.solver.equation_nodes.values():
            all_vars.extend(node.variables)
        
        from collections import Counter
        var_counts = Counter(all_vars)
        print("\nMost common variables:")
        for var, count in var_counts.most_common(10):
            print(f"  {var}: {count}")
        
        # Connection statistics
        cursor.execute("SELECT COUNT(*) FROM connections")
        total_conn = cursor.fetchone()[0]
        print(f"\nTotal connections: {total_conn}")
        
        # Most connected equations
        cursor.execute('''
            SELECT e.equation, COUNT(c.id) as connection_count
            FROM equations e
            LEFT JOIN connections c ON e.id = c.from_equation OR e.id = c.to_equation
            GROUP BY e.id
            ORDER BY connection_count DESC
            LIMIT 5
        ''')
        
        print("\nMost connected equations:")
        for eq, count in cursor.fetchall():
            print(f"  {eq[:40]}... ({count} connections)")
        
        conn.close()
    
    def export_tree(self):
        """Export knowledge tree."""
        print("\n" + "-" * 50)
        print("EXPORT KNOWLEDGE TREE")
        print("-" * 50)
        
        output_path = input("Enter output file name (default: knowledge_tree.json): ").strip()
        if not output_path:
            output_path = "knowledge_tree.json"
        
        print("Exporting knowledge tree...")
        tree = self.solver.export_knowledge_tree(output_path)
        
          print(f"\nExported {len(tree['equations'])} equations and {len(tree['connections'])} connections")
        print(f"to {output_path}")
        
        # Show summary
        print("\nExport summary:")
        print(f"  Total equations: {len(tree['equations'])}")
        print(f"  Total connections: {len(tree['connections'])}")
        print(f"  PRI conservation constant: {tree['metadata']['pri_framework']['conservation_constant']}")
        print(f"  Golden ratio: {tree['metadata']['sacred_geometry']['golden_ratio']:.6f}")
    
    def find_connections(self):
        """Find connections between equations."""
        print("\n" + "-" * 50)
        print("FIND CONNECTIONS BETWEEN EQUATIONS")
        print("-" * 50)
        
        if len(self.solver.equation_nodes) < 2:
            print("Need at least 2 equations to find connections.")
            return
        
        # List equations
        print("\nAvailable equations:")
        eq_list = list(self.solver.equation_nodes.items())
        for i, (eq_id, node) in enumerate(eq_list[:20], 1):
            print(f"{i}. {node.equation[:50]}... ({node.domain})")
        
        if len(eq_list) > 20:
            print(f"... and {len(eq_list) - 20} more")
        
        # Select first equation
        try:
            idx1 = int(input("\nSelect first equation (number): ")) - 1
            if idx1 < 0 or idx1 >= len(eq_list):
                print("Invalid selection.")
                return
            eq_id1, node1 = eq_list[idx1]
        except ValueError:
            print("Invalid input.")
            return
        
        # Select second equation
        try:
            idx2 = int(input("Select second equation (number): ")) - 1
            if idx2 < 0 or idx2 >= len(eq_list):
                print("Invalid selection.")
                return
            eq_id2, node2 = eq_list[idx2]
        except ValueError:
            print("Invalid input.")
            return
        
        if eq_id1 == eq_id2:
            print("Cannot find connections between the same equation.")
            return
        
        print(f"\nFinding connections between:")
        print(f"1. {node1.equation}")
        print(f"2. {node2.equation}")
        
        # Find paths
        paths = self.solver.find_interconnections(eq_id1, eq_id2, max_paths=5)
        
        if not paths:
            print("\nNo direct connections found.")
            
            # Check for indirect connections through shared variables
            shared_vars = set(node1.variables) & set(node2.variables)
            if shared_vars:
                print(f"\nShared variables: {', '.join(shared_vars)}")
                print("These equations can be connected through these variables.")
            
            # Check for sacred number connections
            if node1.sacred_number and node2.sacred_number and node1.sacred_number == node2.sacred_number:
                sacred = SacredNumber(node1.sacred_number)
                print(f"\nBoth equations contain sacred number {node1.sacred_number} ({sacred.value[1]})")
            
            return
        
        print(f"\nFound {len(paths)} connection path(s):")
        
        for i, path in enumerate(paths, 1):
            print(f"\nPath {i} ({len(path)-1} steps):")
            for j, eq_id in enumerate(path):
                node = self.solver.equation_nodes[eq_id]
                
                # Get connection type to next node
                if j < len(path) - 1:
                    next_id = path[j + 1]
                    edge_data = self.solver.knowledge_graph.get_edge_data(eq_id, next_id)
                    conn_type = ""
                    if edge_data:
                        for key in edge_data:
                            conn_type = edge_data[key].get('connection_type', '')
                            break
                else:
                    conn_type = ""
                
                prefix = "  " * j + "→ " if j > 0 else ""
                print(f"{prefix}[{node.domain.upper()}] {node.equation}")
                
                if conn_type:
                    print("  " * (j + 1) + f"Connection: {conn_type}")
            
            # Calculate path significance
            significance = self._calculate_path_significance(path)
            print(f"  Path significance: {significance:.2f}/1.0")
            
            # Show how equations can be combined
            self._show_equation_combination(path)
    
    def _calculate_path_significance(self, path: List[str]) -> float:
        """Calculate significance score for a connection path."""
        score = 0.0
        
        for i in range(len(path) - 1):
            eq1 = self.solver.equation_nodes[path[i]]
            eq2 = self.solver.equation_nodes[path[i + 1]]
            
            # Shared variables
            shared_vars = set(eq1.variables) & set(eq2.variables)
            score += len(shared_vars) * 0.2
            
            # Sacred number connection
            if eq1.sacred_number and eq2.sacred_number and eq1.sacred_number == eq2.sacred_number:
                score += 0.3
            
            # Same domain
            if eq1.domain == eq2.domain:
                score += 0.1
            
            # Geometry pattern match
            if eq1.geometry_pattern and eq2.geometry_pattern and eq1.geometry_pattern == eq2.geometry_pattern:
                score += 0.2
        
        # Normalize to 0-1
        return min(score, 1.0)
    
    def _show_equation_combination(self, path: List[str]):
        """Show how equations in path can be combined."""
        if len(path) < 2:
            return
        
        print("\nEquation combination:")
        
        # Collect all variables along the path
        all_vars = set()
        for eq_id in path:
            all_vars.update(self.solver.equation_nodes[eq_id].variables)
        
        # Try to create a combined equation
        combined_vars = list(all_vars)
        if len(combined_vars) <= 5:  # Only show if manageable
            print(f"  Variables involved: {', '.join(combined_vars)}")
            
            # Show how they could be related
            print("  Potential relationship: ", end="")
            
            # Check for common patterns
            eqs = [self.solver.equation_nodes[eq_id] for eq_id in path]
            
            # Look for conservation laws
            conserved = []
            for var in combined_vars:
                if any(var in eq.variables for eq in eqs):
                    # Check if this variable appears in multiple equations
                    eqs_with_var = [eq for eq in eqs if var in eq.variables]
                    if len(eqs_with_var) > 1:
                        conserved.append(var)
            
            if conserved:
                print(f"Conservation of {', '.join(conserved)}")
            else:
                print("Interconnected system of equations")
            
            # Suggest solving strategy
            print("  Solving strategy: Solve sequentially along the path")

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Theory of Everything Equation Solver with PRI Framework'
    )
    
    parser.add_argument(
        '--input', '-i',
        help='Input file or directory containing equations'
    )
    
    parser.add_argument(
        '--solve', '-s',
        help='Solve for variable (format: "variable=equation" or just variable if equation in DB)'
    )
    
    parser.add_argument(
        '--known', '-k',
        nargs='*',
        help='Known variables (format: "var=value")'
    )
    
    parser.add_argument(
        '--visualize', '-v',
        action='store_true',
        help='Generate sacred geometry visualization'
    )
    
    parser.add_argument(
        '--export', '-e',
        help='Export knowledge tree to JSON file'
    )
    
    parser.add_argument(
        '--interactive', '-I',
        action='store_true',
        help='Launch interactive mode'
    )
    
    parser.add_argument(
        '--pri-explore',
        action='store_true',
        help='Explore PRI framework with specific value'
    )
    
    parser.add_argument(
        '--pri-value',
        type=float,
        help='Value to explore with PRI framework'
    )
    
    args = parser.parse_args()
    
    if args.interactive or not any(vars(args).values()):
        # Launch interactive CLI
        cli = InteractiveTheoryCLI()
        cli.run()
        return
    
    # Non-interactive mode
    solver = TheoryOfEverythingSolver()
    
    # Import equations if specified
    if args.input:
        if os.path.isdir(args.input):
            for file in Path(args.input).glob('*'):
                if file.suffix.lower() in ['.pdf', '.txt', '.docx', '.doc', '.odt', '.jpg', '.jpeg', '.png', '.gif']:
                    try:
                        count = solver.import_equations_from_file(str(file), 'auto')
                        print(f"Imported {count} equations from {file.name}")
                    except Exception as e:
                        print(f"Error importing {file}: {e}")
        else:
            count = solver.import_equations_from_file(args.input, 'auto')
            print(f"Imported {count} equations from {args.input}")
    
    # Solve if specified
    if args.solve:
        known_vars = {}
        if args.known:
            for kv in args.known:
                if '=' in kv:
                    var, val = kv.split('=', 1)
                    try:
                        known_vars[var.strip()] = float(val.strip())
                    except ValueError:
                        print(f"Invalid value for {var}: {val}")
        
        if '=' in args.solve:
            # Equation provided directly
            var, eq = args.solve.split('=', 1)
            var = var.strip()
            
            # Add equation to solver
            eq_id = hashlib.md5(eq.encode()).hexdigest()[:16]
            node = EquationNode(
                id=eq_id,
                equation=eq.strip(),
                asciimath=eq.strip(),
                domain="unknown",
                variables=solver._extract_variables_from_asciimath(eq.strip()),
                source="command_line"
            )
            solver.add_equation(node)
            
            result = solver.solve_system(var, known_vars)
        else:
            # Solve for variable using equations in database
            result = solver.solve_system(args.solve, known_vars)
        
        if result['success']:
            print(f"\nSolution found: {args.solve} = {result['value']}")
            
            if 'solution_path' in result:
                print("\nSolution path:")
                for step in result['solution_path']:
                    print(f"  {step['equation']}")
                    print(f"    → {step['variable']} = {step['solution']}")
                    
                    if step.get('pri_form'):
                        print(f"    PRI form: {step['pri_form']}")
                    
                    if step.get('sacred_connections'):
                        print(f"    Sacred: {', '.join(step['sacred_connections'])}")
                    
                    print()
        else:
            print(f"\nFailed to solve: {result.get('error', 'Unknown error')}")
    
    # Explore PRI framework
    if args.pri_explore and args.pri_value:
        fence = solver.pri.fence_manifold(args.pri_value)
        print(f"\nPRI Fence Manifold for {args.pri_value}:")
        print(f"  1/{args.pri_value} = {fence['primary_state']['value']}")
        print(f"  {fence['reciprocal_state']['value']}/1 = {fence['reciprocal_state']['value']}")
        print(f"  Conservation constant S = {fence['conservation_constant']['S']}")
        
        if fence['sacred_check']['is_sacred']:
            print(f"\nSacred properties:")
            for prop in fence['sacred_check']['properties']:
                print(f"  • {prop}")
    
    # Generate visualization
    if args.visualize:
        solver.generate_sacred_geometry_visualization("theory_of_everything.png")
        print("Generated sacred geometry visualization: theory_of_everything.png")
    
    # Export knowledge tree
    if args.export:
        tree = solver.export_knowledge_tree(args.export)
        print(f"Exported knowledge tree to {args.export}")
        print(f"  Equations: {len(tree['equations'])}")
        print(f"  Connections: {len(tree['connections'])}")

if __name__ == "__main__":
    # Create necessary directories
    os.makedirs('exports', exist_ok=True)
    os.makedirs('visualizations', exist_ok=True)
    
    print("=" * 70)
    print("THEORY OF EVERYTHING EQUATION SOLVER")
    print("With Persistent Reciprocal Identity Framework")
    print("Sacred Geometry & Sumerian Base-60 Integration")
    print("=" * 70)
    print()
    
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        print(f"\nFatal error occurred: {e}")
        print("Check theory_of_everything.log for details.")
