/*

Uses Gurobi optimization solver.

A simple example to add a decision variable to an existing optimization problem.

Solve 
      max 3x + 2z st
        2x +  z <= 18
        2x + 3z <= 42
        3x +  z <= 24
        x >= 0
        z >= 0

And,

Solve 
      max 3x + 2z + 0y st
        2x +  z + 0y <= 18
        2x + 3z + 2y <= 42
        3x +  z + 2y <= 24
        x >= 0
        z >= 0
        y >= 1
        
*/
import gurobi.*;

public class AddVarConstraintExample {

  public static void main(String[] args) {
    try {


      String decVarNames[] =
          new String[] { "x","z"};
      int ndecVarNames = decVarNames.length;
      double cost[] =
          new double[] {
            3,
            2
          };
      String constraintNames[] =
          new String[] {"first","second","third"};
      int nConstraints = constraintNames.length;
      double constraintCoeffs[][] = new double[][] {
        {2,1},
        {2,3},
        {3,1}
      };
      double constraintRHS[] = new double[] {
        18,
        42,
        24
      };

      // Model
      GRBEnv env = new GRBEnv();
      GRBModel model = new GRBModel(env);
      model.set(GRB.StringAttr.ModelName, "add variable and constraints example");

      GRBVar[] decision = new GRBVar[ndecVarNames];
      for (int i = 0; i < ndecVarNames; ++i) {
        decision[i] =
            model.addVar(0, GRB.INFINITY, cost[i], GRB.CONTINUOUS,
                         decVarNames[i]);
      }

      //maximize
      model.set(GRB.IntAttr.ModelSense, -1);

      // Update model to integrate new variables
      model.update();

      //constraints
      GRBLinExpr constraint[] = new GRBLinExpr[nConstraints];
      for (int i = 0; i < nConstraints; ++i) {
        constraint[i] = new GRBLinExpr();
        for (int j = 0; j < ndecVarNames; ++j) {
          constraint[i].addTerm(constraintCoeffs[i][j], decision[j]);
        }
        model.addConstr(constraint[i], GRB.LESS_EQUAL, constraintRHS[i], constraintNames[i]);
      }

      // Solve
      model.optimize();
      printSolution(model, decision);

      //Adding a new variable and constraints
      String newVarName = "y";
      double newCost = 0;
      double newLB = 1;
      System.out.println("\nAdding new var: "+newVarName);
      GRBVar[] newDecision = new GRBVar[1];
      newDecision[0] = model.addVar(newLB,GRB.INFINITY,newCost,GRB.CONTINUOUS,newVarName);//CRITICAL STEP
      model.update();//CRITIAL STEP
      double newConstraintCoeffsAddendum[] = new double[] {0,2,2};
      for (int i = 0; i < nConstraints; ++i) {
        constraint[i].addTerm(newConstraintCoeffsAddendum[i],newDecision[0]);//CRITICAL STEP
        model.addConstr(constraint[i], GRB.LESS_EQUAL, constraintRHS[i], constraintNames[i]);
      }

      // Solve
      model.optimize();
      printSolution(model, concatGRBVar(decision,newDecision));

    
      // Dispose off model and environment
      model.dispose();
      env.dispose();

    } catch (GRBException e) {
      System.out.println("Error code: " + e.getErrorCode() + ". " +
          e.getMessage());
    }
  }

  private static void printSolution(GRBModel model, GRBVar[] decision) throws GRBException {
    if (model.get(GRB.IntAttr.Status) == GRB.Status.OPTIMAL) {
      System.out.println("\nCost: " + model.get(GRB.DoubleAttr.ObjVal));
      System.out.println("\nDecision:");
      for (int j = 0; j < decision.length; ++j) {
          System.out.println(decision[j].get(GRB.StringAttr.VarName) + " " +
              decision[j].get(GRB.DoubleAttr.X));
      }
    } else {
      System.out.println("No solution");
    }
  }

  public static GRBVar[] concatGRBVar(GRBVar[] A, GRBVar[] B) {
   int aLen = A.length;
   int bLen = B.length;
   GRBVar[] C= new GRBVar[aLen+bLen];
   System.arraycopy(A, 0, C, 0, aLen);
   System.arraycopy(B, 0, C, aLen, bLen);
   return C;
}

}
